from typing import Any

import discord


class SendHelpMessage:
    async def execute(self, event_obj: Any):
        embed_message = discord.Embed(
            title="📜 Lista de Comandos",
            color=16775424,
            description="Use os comandos abaixo:",
        )

        embed_message.add_field(
            name="🔹 bob!skill _X Y_",
            value=(
                "Lista o resumo de experiência dos últimos 12 meses.\n"
                "_X = skill_ | _Y = nome do personagem_"
            ),
            inline=False,
        )

        embed_message.add_field(
            name="🔹 bob!profile _X_",
            value=(
                "Mostra o resumo do perfil do jogador.\n" "_X = nome do personagem_"
            ),
            inline=False,
        )

        embed_message.add_field(
            name="🔹 bob!playercount",
            value="Exibe o número de jogadores online no RS3 e OSRS.",
            inline=False,
        )

        embed_message.add_field(
            name="🔹 bob!ge itemgraph _X_",
            value=(
                "Mostra o gráfico de preço do item nos últimos 180 dias.\n"
                "_X = nome do item_"
            ),
            inline=False,
        )

        embed_message.add_field(
            name="🔹 bob!ge iteminfo _X_",
            value=(
                "Mostra preço atual + informações de mercado.\n" "_X = nome do item_"
            ),
            inline=False,
        )

        embed_message.add_field(
            name="🔹 bob!news X",
            value=(
                "Retorna as **X notícias mais recentes** do RuneScape 3.\n"
                "• `X` define a quantidade de notícias exibidas\n"
                "• Valor máximo permitido: **10** (valores maiores serão limitados automaticamente)"
            ),
            inline=False,
        )

        await event_obj.channel.send(embed=embed_message)
