from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class ArgentineBanksAdapter:
    @staticmethod
    def get_response_by_url(url: str) -> BeautifulSoup:
        header = {"User-Agent": "Mozilla/5.0"}
        request = Request(url, headers=header)
        webpage = urlopen(request, timeout=5).read()
        return BeautifulSoup(webpage, "html.parser")
