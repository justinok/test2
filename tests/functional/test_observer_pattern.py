from src import main, publisher, subscribers

event = publisher.EventManager()
user_interface = subscribers.UserInterface()
logger = subscribers.Logger()
alert_system = subscribers.AlertSystem()
weather_station = main.WeatherStation()

event.subscribe(publisher.EventType.TEMPERATURE, user_interface)
event.subscribe(publisher.EventType.HUMIDITY, user_interface)

event.subscribe(publisher.EventType.TEMPERATURE, logger)
event.subscribe(publisher.EventType.WIND_SPEED, logger)
event.subscribe(publisher.EventType.PRESSURE, logger)
event.subscribe(publisher.EventType.HUMIDITY, logger)

event.subscribe(publisher.EventType.TEMPERATURE, alert_system)
event.subscribe(publisher.EventType.WIND_SPEED, alert_system)

weather_station.set_event_manager(event)

weather_station.set_temperature(new_temperature=38.5)
weather_station.set_wind_speed(new_wind_speed=4.0)
weather_station.set_humidity(new_humidity=0.5)
weather_station.set_pressure(new_pressure=101.24)


class TestObserverPattern:
    def test_correct_value(self):
        expected_display = "Temperature: 38.5\nHumidity: 0.5\n"

        expected_log = (
            "[LOG] Temperature: 38.5\n[LOG] Wind Speed: 4.0\n"
            "[LOG] Pressure: 101.24\n[LOG] Humidity: 0.5\n"
        )
        expected_alert = "[ALERT] Temperature: 38.5\n[ALERT] Wind Speed: 4.0\n"

        actual_display = user_interface.display()
        actual_log = logger.log()
        actual_alert = alert_system.alert()

        assert (
            expected_display == actual_display
        ), f"Wrong value. Expected {expected_display} "
        f"but got {actual_display}."

        assert (
            expected_log == actual_log
        ), f"Wrong value. Expected {expected_log} "
        f"but got {actual_log}."

        assert (
            expected_alert == actual_alert
        ), f"Wrong value. Expected {expected_alert} "
        f"but got {actual_alert}."
