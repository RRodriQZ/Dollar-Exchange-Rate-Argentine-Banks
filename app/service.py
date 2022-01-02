from app.constants import ARGENTINE_BANKS_LIST
from app.adapter import ArgentineBanksAdapter
from bs4 import BeautifulSoup
import datetime
import re


class ArgentineBanksService:
    def get_dollar_values_of_banks(self) -> dict:
        banks_list = []
        for url in ARGENTINE_BANKS_LIST:
            try:
                response = ArgentineBanksAdapter.get_response_by_url(url)
                name_bank = self.__get_name_bank_by_url(url)
                value_list = self.__get_value_format_scrapping(response)

                bank_info = {
                    "0.Banco": name_bank,
                    "1.Fecha": datetime.datetime.now(),
                    "2.Compra ($)": value_list[0],
                    "3.Venta ($)": value_list[1],
                    "4.Valor de compra parcial ($)": value_list[2],
                    "5.Valor de compra final ($)": value_list[3],
                }
                banks_list.append(bank_info)
            except:
                pass
        return banks_list

    def __get_name_bank_by_url(self, url: str) -> str:
        url_bank = re.split(
            "https://www.infodolar.com/cotizacion-dolar-entidad-|.aspx", url
        )
        return url_bank[1].upper()

    def __get_value_format_scrapping(self, response: BeautifulSoup) -> list[float]:
        partial_list = []
        for i in range(0, 4):
            dollar_value = (
                response.find("table")
                .find_all("td", {"class": "colCompraVenta"})[i]
                .text
            )
            format_value = ((dollar_value.strip()).split(" "))[1].replace(",", ".")
            value_split = format_value.split("\r\n")[0]
            value = round(float(value_split.replace(",", ".")), 2)
            partial_list.append(value)

        return partial_list
