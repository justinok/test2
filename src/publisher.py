import enum
from typing import Dict, List

from src import subscribers


class EventType(str, enum.Enum):
    TEMPERATURE = "temperature"
    WIND_SPEED = "wind_speed"
    PRESSURE = "pressure"
    HUMIDITY = "humidity"


class EventManager:
    def __init__(self) -> None:
        self._listeners = {event: [] for event in EventType}

    def subscribe(
        self, event_type: EventType, listener: subscribers.EventListener
    ) -> None:
        self._listeners[event_type].append(listener)

    def notify(self, event_type: EventType, data: float) -> None:
        for listener in self._listeners[event_type]:
            listener.update(event_type.value, data)
