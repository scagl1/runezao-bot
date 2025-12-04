from abc import ABC, abstractmethod
from typing import Any


class EventListener(ABC):
    @abstractmethod
    async def handle_event(self, event_name: str, event_obj: Any):
        pass
