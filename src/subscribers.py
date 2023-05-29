import abc


class EventListener(abc.ABC):
    @abc.abstractmethod
    def update(self, event_type: str, new_value: float) -> None:
        pass


class UserInterface(EventListener):
    def __init__(self) -> None:
        self._temperature: float = 0
        self._humidity: float = 0

    def update(self, event_type: str, new_value: float) -> None:
        if event_type == "temperature":
            self._temperature = new_value
        elif event_type == "humidity":
            self._humidity = new_value

    def display(self) -> str:
        return f"Temperature: {self._temperature}\n" f"Humidity: {self._humidity}\n"


class Logger(EventListener):
    def __init__(self) -> None:
        self._temperature: float = 0
        self._wind_speed: float = 0
        self._pressure: float = 0
        self._humidity: float = 0

    def update(self, event_type: str, new_value: float) -> None:
        if event_type == "temperature":
            self._temperature = new_value
        elif event_type == "wind_speed":
            self._wind_speed = new_value
        elif event_type == "pressure":
            self._pressure = new_value
        elif event_type == "humidity":
            self._humidity = new_value

    def log(self) -> str:
        return (
            f"[LOG] Temperature: {self._temperature}\n"
            f"[LOG] Wind Speed: {self._wind_speed}\n"
            f"[LOG] Pressure: {self._pressure}\n"
            f"[LOG] Humidity: {self._humidity}\n"
        )


class AlertSystem(EventListener):
    def __init__(self) -> None:
        self._temperature: float = 0
        self._wind_speed: float = 0

    def update(self, event_type: str, new_value: float) -> None:
        if event_type == "temperature":
            self._temperature = new_value
        elif event_type == "wind_speed":
            self._wind_speed = new_value

    def alert(self) -> str:
        return f"[ALERT] Temperature: {self._temperature}\n" f"[ALERT] Wind Speed: {self._wind_speed}\n"
