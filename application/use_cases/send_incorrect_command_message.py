from typing import Any


class SendIncorrectCommandMessage:
    __incorrect_command_message = """
  Desculpe, não consegui entender o que você disse.
Pode ser que algum comando descrito ainda não esteja implementado :(
  """

    async def execute(self, event_obj: Any):
        await event_obj.channel.send(self.__incorrect_command_message)
