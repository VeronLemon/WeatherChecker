import unittest

from application.weather_service import WeatherService

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.service = WeatherService()

    def test_temperature(self):
        results = self.service.analyze_text("Сегодня -5°C, ясно.")
        self.assertEqual(results[0].temperature, -5)

    def test_condition(self):
        results = self.service.analyze_text("Сегодня +5°C, облачно.")
        self.assertEqual(results[0].condition, "облачно")

    def test_day(self):
        results = self.service.analyze_text("Завтра +3°C, снег.")
        self.assertEqual(results[0].day, "завтра")

    def test_ignore_line_without_day(self):
        results = self.service.analyze_text("-5°C, снег.")
        self.assertEqual(len(results), 0)

    def test_empty_text(self):
        results = self.service.analyze_text("")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()