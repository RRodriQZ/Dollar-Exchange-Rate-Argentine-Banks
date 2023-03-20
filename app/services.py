from app.constants import ARGENTINE_BANKS
from app.client import BanksClient
from datetime import datetime
from bs4 import BeautifulSoup
from pytz import timezone


class DatetimeService:
    @staticmethod
    def get_time() -> str:
        """
        It returns a string with the current date and time in the timezone
        "America/Argentina/Buenos_Aires"
        :return: A string with the current date and time in the format: YYYY-MM-DD HH:MM:SS
        """
        TIMEZONE: str = "America/Argentina/Buenos_Aires"
        now_bs_as_arg: datetime = datetime.now().astimezone(timezone(TIMEZONE))
        return now_bs_as_arg.strftime("%Y-%m-%d %H:%M:%S")


class ArgentineBanksServices:
    def __get_scrapping_values(self, response: BeautifulSoup) -> list:
        """
        It takes a BeautifulSoup object as an argument, and returns a list of four floats

        :param response: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        :type response: BeautifulSoup
        :return: A list of 4 values, each one is the value of the dollar in the following order:
                - Buy
                - Sell
                - Buy (cash)
                - Sell (cash)
        """
        try:
            VALUES: list = list()

            for i in range(0, 4):
                dollar_value: str = (
                    response.find("table")
                    .find_all("td", {"class": "colCompraVenta"})[i]
                    .text
                )
                format_value: str = (
                    dollar_value.replace(" ", "")
                    .split("\r\n")[1]
                    .replace("$", "")
                    .replace(",", ".")
                )
                value: float = round(float(format_value), 2)
                VALUES.append(value)

            return VALUES

        except:
            return [None, None, None, None]

    def __get_scrapping_date(self, response: BeautifulSoup) -> str:
        """
        It takes a BeautifulSoup object as an argument and returns a string

        :param response: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        :type response: BeautifulSoup
        :return: A datetime.
        """
        try:
            DATE: str = (
                response.find("table")
                .find("td", {"class": "colFecha"})
                .find("abbr", {"class": "timeago date"})
                .text
            )
            return DATE

        except:
            return None

    def get_dollar_values_of_banks(self) -> list:
        """
        It takes a dictionary of banks and their respective urls, and returns a list of dictionaries
        with the name of the bank, the buying and selling values, the partial and final buying values,
        and the date of the last update
        :return: A list of dictionaries.
        """

        BANKS_INFO: list = list()

        for name_bank, url in ARGENTINE_BANKS.items():

            response = BanksClient.get_banks_data(url)

            bank: str = f"Banco-{name_bank}"
            scrapping_values: list = self.__get_scrapping_values(response)
            scrapping_date: str = self.__get_scrapping_date(response)

            bank_info: dict = {
                "1.Banco": bank,
                "2.Compra ($)": scrapping_values[0],
                "3.Venta ($)": scrapping_values[1],
                "4.Valor de compra parcial ($)": scrapping_values[2],
                "5.Valor de compra final ($)": scrapping_values[3],
                "6.Ultima actualizacion": scrapping_date,
            }
            BANKS_INFO.append(bank_info)

        return BANKS_INFO
