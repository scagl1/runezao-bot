from infrastructure.event_listener import EventListener
from typing import Literal, Any
from abc import ABC, abstractmethod


EventName = Literal["message_received"]


class AbstractEventBus(ABC):
    @abstractmethod
    def add_listener(self, event_listener: EventListener) -> None:
        pass

    @abstractmethod
    async def notify_listeners(self, event_name: EventName, event_obj: Any) -> None:
        pass


class EventBus(AbstractEventBus):
    def __init__(self) -> None:
        self.__event_listeners: list[EventListener] = []

    def add_listener(self, event_listener: EventListener) -> None:
        self.__event_listeners.append(event_listener)

    async def notify_listeners(self, event_name: EventName, event_obj: Any) -> None:
        for listener in self.__event_listeners:
            await listener.handle_event(event_name, event_obj)
