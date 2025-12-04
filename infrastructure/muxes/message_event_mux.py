from infrastructure.event_listener import EventListener
from infrastructure.jagex_http_client import JagexHttpClient
from application.text_responses import TextResponses
from typing import Any


class MessageEventMux(EventListener):
    async def handle_event(self, event_name: str, event_obj: Any):
        message_content = event_obj.content
        print(event_name)

        if message_content.startswith("bob!"):
            if "help" in message_content:
                await self.handle_list_help(event_obj=event_obj)
                return

            if "inspect" in message_content:
                user_name: str = message_content.split()[1]

                if user_name == None:
                    await event_obj.channel.send(
                        TextResponses().get_incorrect_command()
                    )

                await self.handle_inspect_player(
                    event_obj=event_obj, user_name=user_name
                )
                return

            await event_obj.channel.send(TextResponses().get_incorrect_command())

    async def handle_list_help(self, event_obj: Any):
        text = TextResponses().get_help_command_text()
        await event_obj.channel.send(text)

    async def handle_inspect_player(self, event_obj: Any, user_name: str):
        response = JagexHttpClient().get_player_profile(user_name)
        print(response)
        # formatted_text = TextResponses().format_player_inspect_message(response)
        await event_obj.channel.send(response)
