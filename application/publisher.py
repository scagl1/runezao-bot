from application.subscriber import Subscriber
from typing import Literal

EventName = Literal["message_received"]


class Publisher:
    def __init__(self):
        self.__subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    async def notify_subscribers(self, event_name: EventName, event_handler):
        for sub in self.__subscribers:
            await sub.handle_event(event_name, handler=event_handler)
