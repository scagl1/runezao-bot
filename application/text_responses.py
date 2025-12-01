class TextResponses():
  def get_help_command_text(self):
    return """
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
  
  def get_incorrect_command(self):
    return """
  Desculpe, não consegui entender o que você disse.
Pode ser que algum comando descrito ainda não esteja implementado :(
  """