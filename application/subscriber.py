from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    async def handle_event(self, event_name: str, handler):
        pass
