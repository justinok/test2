from typing import Optional

from src import publisher  
from src import subscribers  


class WeatherStation:
    def __init__(self) -> None:
        self._temperature: Optional[float] = None
        self._wind_speed: Optional[float] = None
        self._pressure: Optional[float] = None
        self._humidity: Optional[float] = None
        self._event_manager = publisher.EventManager()
        # instantiating the subscribers (observers)
        self.ui = subscribers.UserInterface()
        self.logger = subscribers.Logger()
        self.alert_system = subscribers.AlertSystem()
        # registering the subscribers with the EventManager
        self._event_manager.subscribe(publisher.EventType.TEMPERATURE, self.ui)
        self._event_manager.subscribe(publisher.EventType.TEMPERATURE, self.logger)
        self._event_manager.subscribe(publisher.EventType.TEMPERATURE, self.alert_system)
        # Similar subscribe calls for other EventTypes (wind speed, pressure, humidity)

    def set_temperature(self, new_temperature):
        self._temperature = new_temperature
        self._event_manager.notify(publisher.EventType.TEMPERATURE, self._temperature)

    def set_wind_speed(self, new_wind_speed):
        self._wind_speed = new_wind_speed
        self._event_manager.notify(publisher.EventType.WIND_SPEED, self._wind_speed)

    def set_pressure(self, new_pressure):
        self._pressure = new_pressure
        self._event_manager.notify(publisher.EventType.PRESSURE, self._pressure)

    def set_humidity(self, new_humidity):
        self._humidity = new_humidity
        self._event_manager.notify(publisher.EventType.HUMIDITY, self._humidity)

    def set_event_manager(self, event_manager: publisher.EventManager):
        self._event_manager = event_manager
