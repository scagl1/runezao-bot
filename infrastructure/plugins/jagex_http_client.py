import requests

from infrastructure.plugins.models.jagex import GetPlayerMonthlyXPModel, GetPlayerProfileModel


class JagexHttpClient:

    def __init__(self) -> None:
        self.jagex_base_url = "https://secure.runescape.com"
        self.apps_url = "https://apps.runescape.com"

    def get_player_monthly_xp(self, user_name: str, skill_id: int) -> GetPlayerMonthlyXPModel:
        """
        Obtém o ganho mensal de experiência de um jogador em uma habilidade específica.

        Args:
            user_name (str): Nome do jogador a ser consultado
            skill_id (int): ID da habilidade

        Returns:
            GetPlayerMonthlyXPModel: histórico anual até o mês atual de XP
            para a habilidade informada
        """
        endpoint = f"{self.apps_url}/runemetrics/xp-monthly?searchName={user_name}&skillid={skill_id}"
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
        endpoint = f"{self.apps_url}/runemetrics/profile/profile?user={user_name}&activities=1"
        response = requests.get(endpoint)
        return response.json()
