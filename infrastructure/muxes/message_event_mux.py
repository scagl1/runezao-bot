from application.use_cases.send_player_profile import SendPlayerProfile
from infrastructure.event_listener import EventListener
from typing import Any
from application.use_cases.send_help_message import SendHelpMessage
from application.use_cases.send_incorrect_command_message import (
    SendIncorrectCommandMessage,
)
from infrastructure.plugins.jagex_http_client import JagexHttpClient


class MessageEventMux(EventListener):
    async def handle_event(self, event_name: str, event_obj: Any) -> None:
        message_content: str = event_obj.content
        print(event_name)

        if message_content.startswith("bob!"):
            if "help" in message_content:
                await SendHelpMessage(event_obj).execute()
                return

            if "profile" in message_content:
                split_message_content = message_content.split(" ")
                if len(split_message_content) < 2:
                    await SendIncorrectCommandMessage(event_obj).execute()
                    return

                player_name = split_message_content[1]
                await SendPlayerProfile(JagexHttpClient()).execute(
                    event_obj, player_name
                )
                return

            await SendIncorrectCommandMessage(event_obj).execute()
