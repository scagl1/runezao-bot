from typing import Any
from infrastructure.plugins.web_scrapper import WebScrapperClient
from infrastructure.plugins.errors.web_scrapper import JagexWebsiteError


class SendRecentNews:
    def __init__(self, web_scrapper_instance: WebScrapperClient) -> None:
        self.__web_scrapper_instance = web_scrapper_instance

    async def execute(self, news_qty: int, event_obj: Any) -> None:
        try:
            news = self.__web_scrapper_instance.scrape_jagex_news_page(news_qty)
        except JagexWebsiteError:
            await event_obj.channel.send("⚠️ Erro detectado no website do RuneScape")
            return

        msg_lines = ["🔎 Encontrei essas aqui:\n"]
        for title, url in news:
            msg_lines.append(title)
            msg_lines.append(url)

        appended_news_msg = "\n".join(msg_lines)
        await event_obj.channel.send(appended_news_msg)
