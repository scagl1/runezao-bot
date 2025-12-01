from application.subscriber import Subscriber
from infrastructure.jagex_http_client import JagexHttpClient
from application.text_responses import TextResponses


class Controller(Subscriber):
    async def handle_event(self, event_name: str, handler):
        message_content = handler.content
        print(f"{event_name}, {message_content}")

        if "help" in message_content:
            await self.handle_list_help(handler)
            return

        await handler.channel.send(TextResponses().get_incorrect_command())

    async def handle_list_help(self, handler):
        text = TextResponses().get_help_command_text()
        await handler.channel.send(text)
