from infrastructure.event_listener import EventListener
from typing import Any
from application.use_cases.send_help_message import SendHelpMessage
from application.use_cases.send_incorrect_command_message import SendIncorrectCommandMessage

class MessageEventMux(EventListener):
    async def handle_event(self, event_name: str, event_obj: Any) -> None:
        message_content = event_obj.content
        print(event_name)

        if message_content.startswith("bob!"):
            if "help" in message_content:
                await SendHelpMessage(event_obj).execute()
                return

            await SendIncorrectCommandMessage(event_obj).execute()
