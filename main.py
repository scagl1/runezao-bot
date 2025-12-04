import os
import logging
from dotenv import load_dotenv
from infrastructure.discord_client import DiscordClient
from infrastructure.event_bus import EventBus
from infrastructure.muxes.message_event_mux import MessageEventMux


def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    if token == None:
        raise Exception("Token vazio")

    logger = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    message_event_mux_instance = MessageEventMux()

    event_bus_instance = EventBus()
    event_bus_instance.add_listener(event_listener=message_event_mux_instance)

    client = DiscordClient(token=token, publisher_instance=event_bus_instance)
    client.run(logger=logger, level=logging.DEBUG)


if __name__ == "__main__":
    main()
