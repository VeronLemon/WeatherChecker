import re

from domain.weather import Weather

class WeatherService:
    TEMPERATURE_PATTERN = (
        r"(?<![\w.])"
        r"(?P<temperature>[+-]?\d{1,2}(?:[.,]\d+)?)"
        r"\s*°?\s*(?:[Cc])?"
        r"(?!\w)"
    )

    CONDITION_PATTERN = (
        r"(?<!\w)"
        r"(?P<condition>"
        r"дождь\s+со\s+снегом|"
        r"снег\s+с\s+дождём|"
        r"снег\s+с\s+дождем|"
        r"небольшой\s+дождь|"
        r"сильный\s+дождь|"
        r"умеренный\s+дождь|"
        r"слабый\s+дождь|"
        r"проливной\s+дождь|"
        r"небольшой\s+снег|"
        r"сильный\s+снег|"
        r"умеренный\s+снег|"
        r"слабый\s+снег|"
        r"малооблачно|"
        r"облачно|"
        r"пасмурно|"
        r"ясно|"
        r"дождь|"
        r"снег"
        r")"
        r"(?!\w)"
    )

    DAY_PATTERN = (
        r"(?<!\w)"
        r"(?P<day>"
        r"сегодня|завтра|"
        r"понедельник(?:а)?|"
        r"вторник(?:а)?|"
        r"сред(?:а|у|ы)|"
        r"четверг(?:а)?|"
        r"пятниц(?:а|у|ы)|"
        r"суббот(?:а|у|ы)|"
        r"воскресень(?:е|я)|"
        r"пн\.?|вт\.?|ср\.?|чт\.?|"
        r"пт\.?|сб\.?|вс\.?"
        r")"
        r"(?!\w)"
    )

    MIN_TEMPERATURE = -90
    MAX_TEMPERATURE = 60

    def is_valid_temperature(self, temperature):
        return (
            self.MIN_TEMPERATURE
            <= temperature
            <= self.MAX_TEMPERATURE
        )

    def analyze_text(self, text):
        results = []

        for line in text.splitlines():
            day_match = re.search(
                self.DAY_PATTERN,
                line,
                re.IGNORECASE
            )

            temperature_match = re.search(
                self.TEMPERATURE_PATTERN,
                line
            )

            condition_match = re.search(
                self.CONDITION_PATTERN,
                line,
                re.IGNORECASE
            )

            day = None
            temperature = None
            condition = None

            if day_match:
                day = day_match.group("day").lower()

            if not day:
                continue

            if temperature_match:
                value = temperature_match.group("temperature")
                value = value.replace(",", ".")
                temperature = float(value)

                if not self.is_valid_temperature(temperature):
                    temperature = None

            if not temperature:
                continue

            if condition_match:
                condition = condition_match.group("condition").lower()

            if day or temperature is not None or condition:
                results.append(
                    Weather(
                        temperature=temperature,
                        condition=condition,
                        day=day
                    )
                )

        return results