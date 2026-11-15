class Weather:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{self.temperature} °C"