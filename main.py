import os
import logging
from dotenv import load_dotenv
from infrastructure.discord_client import DiscordClient
from application.publisher import Publisher
from application.controller import Controller


def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    if token == None:
        raise Exception("Token vazio")

    logger = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    controller_instance = Controller()

    publisher_instance = Publisher()
    publisher_instance.subscribe(controller_instance)

    client = DiscordClient(token=token, publisher_instance=publisher_instance)
    client.run(logger=logger, level=logging.DEBUG)


if __name__ == "__main__":
    main()
