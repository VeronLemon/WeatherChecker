import re

from domain.weather import Weather

class WeatherService:
    TEMPERATURE_PATTERN = (
        r"(?<!\d)(?P<temperature>[+-]?\d{1,2}(?:[.,]\d+)?)"
        r"\s*°\s*[Cc](?!\w)"
    )

    MIN_TEMPERATURE = -90
    MAX_TEMPERATURE = 60

    def find_temperatures(self, text):
        temperatures = []

        matches = re.finditer(self.TEMPERATURE_PATTERN, text)
        for match in matches:
            value = match.group("temperature")
            value = value.replace(",", ".")
            temperature = float(value)
            if self.is_valid_temperature(temperature):
                temperatures.append(Weather(temperature))
        return temperatures

    def is_valid_temperature(self, temperature):
        return (
            self.MIN_TEMPERATURE
            <= temperature
            <= self.MAX_TEMPERATURE
        )