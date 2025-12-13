from datetime import datetime
from typing import Any

import discord

from infrastructure.plugins.jagex_errors import JagexError, PlayerNotFoundError
from infrastructure.plugins.jagex_http_client import JagexHttpClient


class SendPlayerProfile:
    def __init__(self, jagex_client_instance: JagexHttpClient) -> None:
        self.__jagex_client_instance = jagex_client_instance

    async def execute(self, event_obj: Any, player_name: str) -> None:
        try:
            profile = self.__jagex_client_instance.get_player_profile(player_name)
        except PlayerNotFoundError:
            await event_obj.channel.send("❌ Jogador não encontrado")
            return
        except JagexError:
            await event_obj.channel.send("⚠️ Erro de servidores Jagex")
            return

        today_date = datetime.now().strftime("%d/%m/%Y")

        embed_message = discord.Embed(
            title=f"👤 {profile.name}",
            description=f"Perfil de Jogador • {today_date}",
            color=2320281,
        )

        embed_message.add_field(name="🏆 Rank", value=profile.rank)
        embed_message.add_field(
            name="📈 Total de Experiência", value=f"{profile.totalxp:,} XP"
        )
        embed_message.add_field(
            name="📊 Nível total de habilidades", value=f"{profile.totalskill:,}"
        )
        embed_message.add_field(
            name="⚔️ Nível de Combate", value=f"{profile.combatlevel:,}"
        )
        embed_message.add_field(
            name="📜 Missões",
            value=f"""- Completas: {profile.questscomplete}
- Iniciadas: {profile.questsstarted}
- Não iniciadas: {profile.questsnotstarted}""",
        )

        embed_message.set_footer(
            text=self.__jagex_client_instance.get_user_highscore_url(profile.name),
            icon_url=self.__jagex_client_instance.get_user_avatar_url(profile.name),
        )

        await event_obj.channel.send(embed=embed_message)
