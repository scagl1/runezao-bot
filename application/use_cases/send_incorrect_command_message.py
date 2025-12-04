from typing import Any


class SendIncorrectCommandMessage:
    def __init__(self, event_obj: Any):
        self.event_obj = event_obj
        self.__incorrect_command_message = """
  Desculpe, não consegui entender o que você disse.
Pode ser que algum comando descrito ainda não esteja implementado :(
  """

    async def execute(self):
        await self.event_obj.channel.send(self.__incorrect_command_message)
