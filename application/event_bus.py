from infrastructure.event_listener import EventListener
from typing import Literal, Any

EventName = Literal["message_received"]


class EventBus:
    def __init__(self):
        self.__event_listeners: list[EventListener] = []

    def add_listener(self, event_listener: EventListener):
        self.__event_listeners.append(event_listener)

    async def notify_listeners(self, event_name: EventName, event_obj: Any):
        for listener in self.__event_listeners:
            await listener.handle_event(event_name, event_obj)
