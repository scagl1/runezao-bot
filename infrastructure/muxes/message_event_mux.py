from application.use_cases.send_player_count_message import SendPlayerCount
from application.use_cases.send_player_profile import SendPlayerProfile
from application.use_cases.send_recent_news_message import SendRecentNews
from infrastructure.event_listener import EventListener
from typing import Any
from application.use_cases.send_help_message import SendHelpMessage
from application.use_cases.send_incorrect_command_message import (
    SendIncorrectCommandMessage,
)
from infrastructure.plugins.jagex_http_client import JagexHttpClient
from infrastructure.plugins.web_scrapper import WebScrapperClient


class MessageEventMux(EventListener):
    async def handle_event(self, event_name: str, event_obj: Any) -> None:
        message_content: str = event_obj.content
        print(event_name)

        if message_content.startswith("bob!"):
            if "help" in message_content:
                await SendHelpMessage().execute(event_obj)
                return

            if "profile" in message_content:
                split_message_content = message_content.split(" ")
                if len(split_message_content) < 2:
                    await SendIncorrectCommandMessage().execute(event_obj)
                    return

                player_name = split_message_content[1]
                await SendPlayerProfile(JagexHttpClient()).execute(
                    event_obj, player_name
                )
                return

            if "playercount" in message_content:
                await SendPlayerCount(JagexHttpClient()).execute(event_obj)
                return

            if "news" in message_content:
                split_message_content = message_content.split(" ")
                if len(split_message_content) < 2:
                    await SendIncorrectCommandMessage().execute(event_obj)
                    return

                news_qty = int(split_message_content[1])
                await SendRecentNews(WebScrapperClient()).execute(news_qty, event_obj)
                return

            await SendIncorrectCommandMessage().execute(event_obj)
