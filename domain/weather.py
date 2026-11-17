class Weather:
    def __init__(self, temperature=None, condition=None, day=None):
        self.temperature = temperature
        self.condition = condition
        self.day = day

    def __str__(self):
        parts = []

        if self.day:
            parts.append(self.day)

        if self.temperature is not None:
            parts.append(f"{self.temperature} °C")

        if self.condition:
            parts.append(self.condition)

        return ", ".join(parts)