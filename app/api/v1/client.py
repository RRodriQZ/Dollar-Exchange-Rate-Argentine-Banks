from bs4 import BeautifulSoup
import requests


class BanksClient:
    @staticmethod
    def get_banks_data(url: str) -> BeautifulSoup:
        response = requests.get(url=url, timeout=3)
        if response.status_code != 200:
            return None
        return BeautifulSoup(response.content, "html.parser")
