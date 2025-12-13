import requests

from infrastructure.plugins.jagex_errors import JagexError, PlayerNotFoundError
from infrastructure.plugins.models.jagex import (
    GetPlayerMonthlyXPModel,
    GetPlayerProfileModel,
    parse_player_profile,
)


class JagexHttpClient:
    _JAGEX_BASE_URL = "https://secure.runescape.com"
    _APPS_BASE_URL = "https://apps.runescape.com"
    _USER_HIGHSCORE_ENDPOINT = "/m=hiscore/ranking?user="
    _USER_AVATAR_IMG_ENDPOINT = "/m=avatar-rs/$/chat.png"

    def get_user_highscore_url(self, user_name: str) -> str:
        return f"{self._JAGEX_BASE_URL}{self._USER_HIGHSCORE_ENDPOINT}{user_name}"

    def get_user_avatar_url(self, user_name: str) -> str:
        parsed_avatar_endpoint = self._USER_AVATAR_IMG_ENDPOINT.replace("$", user_name)
        return f"{self._JAGEX_BASE_URL}{parsed_avatar_endpoint}"

    def get_player_monthly_xp(
        self, user_name: str, skill_id: int
    ) -> GetPlayerMonthlyXPModel:
        """
        Obtém o ganho mensal de experiência de um jogador em uma habilidade específica.

        Args:
            user_name (str): Nome do jogador a ser consultado
            skill_id (int): ID da habilidade

        Returns:
            GetPlayerMonthlyXPModel: histórico anual até o mês atual de XP
            para a habilidade informada
        """
        endpoint = f"{self._APPS_BASE_URL}/runemetrics/xp-monthly?searchName={user_name}&skillid={skill_id}"
        response = requests.get(endpoint)
        return response.json()

    def get_player_profile(self, user_name: str) -> GetPlayerProfileModel:
        """
        Obtém o perfil completo de um jogador no RuneMetrics

        Args:
            user_name (str): Nome do jogador a ser consultado

        Returns:
            GetPlayerProfileModel: dados do perfil do jogador,
            incluindo níveis, XP, última atividade e ranking
        """
        endpoint = f"{self._APPS_BASE_URL}/runemetrics/profile/profile?user={user_name}&activities=1"
        response = requests.get(endpoint)

        data = response.json()
        if response.status_code != 200:
            raise JagexError

        if "error" in data:
            raise PlayerNotFoundError

        return parse_player_profile(data)
