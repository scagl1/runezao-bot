from logging import FileHandler
import discord
from application.publisher import Publisher

class DiscordClient:
  def __init__(self, token: str, publisher_instance: Publisher):
    self.token = token
    self.intents = discord.Intents.default()
    self.client = discord.Client(intents=self.intents)
    self.intents.message_content = True
    self.client.event(self.on_ready)
    self.client.event(self.on_message)
    self.publisher_instance = publisher_instance
        
  async def on_ready(self):
    print(f'Online and ready to go as {self.client.user}')

  async def on_message(self, message):
    if message.author == self.client.user:
      return

    if message.content.startswith('bob!'):
      await self.publisher_instance.notify_subscribers("msg_received", event_handler=message)

  def run(self, logger: FileHandler, level: int):
    self.client.run(token=self.token, log_handler=logger, log_level=level)