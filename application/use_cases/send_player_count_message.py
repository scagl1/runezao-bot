from datetime import datetime
from typing import Any

import discord

from infrastructure.plugins.errors.jagex_http_client import JagexError
from infrastructure.plugins.jagex_http_client import JagexHttpClient


class SendPlayerCount:

    def __init__(self, jagex_client_instance: JagexHttpClient) -> None:
        self.__jagex_client_instance = jagex_client_instance

    async def execute(self, event_obj: Any) -> None:
        try:
            player_count = self.__jagex_client_instance.get_player_count()
        except JagexError:
            await event_obj.channel.send("⚠️ Erro de servidores Jagex")
            return

        today_datetime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        embed_message = discord.Embed(
            title=f"🌐 Jogadores Online • {today_datetime}", color=1900288
        )
        embed_message.add_field(
            name="RuneScape + Old School RuneScape", value=player_count
        )
        embed_message.set_footer(
            text=self.__jagex_client_instance.PLAYER_COUNT_URL,
            icon_url=self.__jagex_client_instance.RUNESCAPE_ICON_IMAGE_URL,
        )

        await event_obj.channel.send(embed=embed_message)
