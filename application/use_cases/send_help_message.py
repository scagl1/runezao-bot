from typing import Any


class SendHelpMessage:
    def __init__(self, event_obj: Any):
        self.event_obj = event_obj
        self.__help_command_message = """
      **📜 Lista de Comandos**

    • **bob!skill _X Y_**
      Lista o resumo de experiência dos últimos 12 meses.  
      _X = skill_ | _Y = nome do personagem_

    • **bob!inspect _X_**
      Mostra o resumo do perfil do jogador.
      _X = nome do personagem_

    • **bob!playercount**
      Exibe o número de jogadores online no RS3 e OSRS.

    • **bob!ge itemgraph _X_**
      Mostra o gráfico de preço do item nos últimos 180 dias.
      _X = nome do item_

    • **bob!ge iteminfo _X_**
      Mostra preço atual + informações de mercado.
      _X = nome do item_

    • **bob!news**
      Retorna as 3 notícias mais recentes do RuneScape 3.
      """

    async def execute(self):
        await self.event_obj.channel.send(self.__help_command_message)
