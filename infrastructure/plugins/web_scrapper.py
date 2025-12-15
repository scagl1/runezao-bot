import requests
from bs4 import BeautifulSoup

from infrastructure.plugins.errors.web_scrapper import JagexWebsiteError


class WebScrapperClient:
    __JAGEX_NEWS_URL = "https://secure.runescape.com/m=news/?cat=10&page=1"

    def scrape_jagex_news_page(self, news_qty: int) -> list[tuple[str, str]]:
        response = requests.get(self.__JAGEX_NEWS_URL)

        if response.status_code != 200:
            raise JagexWebsiteError

        soup = BeautifulSoup(response.text, "html.parser")

        news_anchor_elements = soup.find_all(
            "a", class_="news-list-article__title-link"
        )[:news_qty]

        news_tuples = []
        for title in news_anchor_elements:
            news_title = title.get_text(strip=True)
            news_link = title.get_attribute_list("href")[0]
            news_tuples.append((news_title, news_link))

        return news_tuples
