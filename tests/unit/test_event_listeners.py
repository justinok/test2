from src import subscribers

user_interface = subscribers.UserInterface()
logger = subscribers.Logger()
alert_system = subscribers.AlertSystem()


class TestUpdateUserInterface:
    def test_correct_temperature_type(self):
        user_interface.update("temperature", 37.5)
        actual = user_interface._temperature
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_temperature_value(self):
        expected = 37.5
        user_interface.update("temperature", expected)
        actual = user_interface._temperature
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."

    def test_correct_humidity_type(self):
        user_interface.update("humidity", 0.9)
        actual = user_interface._humidity
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_humidity_value(self):
        expected = 0.9
        user_interface.update("humidity", expected)
        actual = user_interface._humidity
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestDisplayUserInterface:
    def test_correct_type(self):
        actual = user_interface.display()
        assert isinstance(
            actual, str
        ), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        expected = "Temperature: 37.5\nHumidity: 0.9\n"
        actual = user_interface.display()
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestUpdateLog:
    def test_correct_temperature_type(self):
        logger.update("temperature", 37.5)
        actual = logger._temperature
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_temperature_value(self):
        expected = 37.5
        logger.update("temperature", expected)
        actual = logger._temperature
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."

    def test_correct_wind_speed_type(self):
        logger.update("wind_speed", 5.0)
        actual = logger._wind_speed
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_wind_speed_value(self):
        expected = 5.0
        logger.update("wind_speed", expected)
        actual = logger._wind_speed
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."

    def test_correct_pressure_type(self):
        logger.update("pressure", 101.325)
        actual = logger._pressure
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_pressure_value(self):
        expected = 101.325
        logger.update("pressure", expected)
        actual = logger._pressure
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."

    def test_correct_humidity_type(self):
        logger.update("humidity", 0.9)
        actual = logger._humidity
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_humidity_value(self):
        expected = 0.9
        logger.update("humidity", expected)
        actual = logger._humidity
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestLog:
    def test_correct_type(self):
        actual = logger.log()
        assert isinstance(
            actual, str
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_value(self):
        expected = (
            "[LOG] Temperature: 37.5\n[LOG] Wind Speed: 5.0\n"
            "[LOG] Pressure: 101.325\n[LOG] Humidity: 0.9\n"
        )
        actual = logger.log()
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestUpdateAlertSystem:
    def test_correct_temperature_type(self):
        alert_system.update("temperature", 37.5)
        actual = alert_system._temperature
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_temperature_value(self):
        expected = 37.5
        alert_system.update("temperature", expected)
        actual = alert_system._temperature
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."

    def test_correct_wind_speed_type(self):
        alert_system.update("wind_speed", 5.0)
        actual = alert_system._wind_speed
        assert isinstance(
            actual, float
        ), f"Wrong type. Expected 'float', got {type(actual)}"

    def test_correct_wind_speed_value(self):
        expected = 5.0
        alert_system.update("wind_speed", expected)
        actual = alert_system._wind_speed
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."


class TestAlert:
    def test_correct_type(self):
        actual = alert_system.alert()
        assert isinstance(
            actual, str
        ), f"Wrong type. Expected 'str', got {type(actual)}"

    def test_correct_value(self):
        expected = "[ALERT] Temperature: 37.5\n[ALERT] Wind Speed: 5.0\n"
        actual = alert_system.alert()
        assert (
            expected == actual
        ), f"Wrong value. Expected {expected} but got {actual}."
