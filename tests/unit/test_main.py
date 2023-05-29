from src import main, publisher

weather_station = main.WeatherStation()


class TestSetTemperature:
    def test_correct_type(self):
        weather_station.set_temperature(37.5)
        actual = weather_station._temperature
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        expected = 37.5
        weather_station.set_temperature(expected)
        actual = weather_station._temperature
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestSetWindSpeed:
    def test_correct_type(self):
        weather_station.set_wind_speed(5.0)
        actual = weather_station._wind_speed
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        expected = 5.0
        weather_station.set_wind_speed(expected)
        actual = weather_station._wind_speed
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestSetPressure:
    def test_correct_type(self):
        weather_station.set_pressure(101.325)
        actual = weather_station._pressure
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        expected = 101.325
        weather_station.set_pressure(expected)
        actual = weather_station._pressure
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestSetHumidity:
    def test_correct_type(self):
        weather_station.set_humidity(0.9)
        actual = weather_station._humidity
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        expected = 0.9
        weather_station.set_humidity(expected)
        actual = weather_station._humidity
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestSetEventManager:
    def test_correct_type(self):
        event = publisher.EventManager()
        weather_station.set_event_manager(event)
        actual = weather_station.event_manager
        assert isinstance(
            actual, publisher.EventManager
        ), f"Wrong type. Expected 'float', got {type(actual)}"
