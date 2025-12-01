import requests


class JagexHttpClient:

    def __init__(self):
        self.wiki_base_url = "https://runescape.wiki/api.php"
        self.jagex_base_url = "https://secure.runescape.com"
        self.apps_url = "https://apps.runescape.com"

    def fuzzy_get_item_by_name(self, item_name: str):
        """_summary_

        Args:
            item_name (str): _description_
        """
        endpoint = f"{self.wiki_base_url}?action=query&format=json&list=search&srsearch={item_name}"
        response = requests.get(endpoint)
        return response.json()

    def get_player_monthly_xp(self, user_name: str, skill_id: int):
        """_summary_
        Retorna a quantidade de experiência
        """
        endpoint = f"{self.apps_url}/runemetrics/xp-monthly?searchName={user_name}&skillid={skill_id}"
        response = requests.get(endpoint)
        return response.json()
