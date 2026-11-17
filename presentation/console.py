from application.weather_service import WeatherService
from infrastructure.text_repository import TextRepository

class Console:
    def __init__(self):
        self.weather_service = WeatherService()
        self.repository = TextRepository()

    def show_menu(self):
        print("\n=== ПРОВЕРКА ПОГОДЫ ===")
        print("1. Поиск в тексте")
        print("2. Поиск в файле")
        print("3. Поиск на веб-странице")
        print("0. Выход")

    def show_results(self, text):
        results = self.weather_service.analyze_text(text)

        if not results:
            print("Данные о погоде не найдены.")
            return

        for result in results:
            parts = []

            if result.day:
                parts.append(result.day.capitalize())

            if result.temperature is not None:
                parts.append(f"{result.temperature:g} °C")

            if result.condition:
                parts.append(result.condition)

            print(" | ".join(parts))

    def search_in_text(self):
        text = input("\nВведите текст: ")
        self.show_results(text)

    def search_in_file(self):
        path = input("\nВведите путь к файлу: ")

        try:
            text = self.repository.get_text(path)
            self.show_results(text)
        except (FileNotFoundError, PermissionError) as error:
            print(f"Ошибка: {error}")

    def search_on_webpage(self):
        url = input("\nВведите URL веб-страницы: ")

        try:
            text = self.repository.get_text_from_url(url)
            self.show_results(text)
        except ValueError as error:
            print(f"Ошибка: {error}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.search_in_text()
            elif choice == "2":
                self.search_in_file()
            elif choice == "3":
                self.search_on_webpage()
            elif choice == "0":
                print("Программа завершена!")
                break
            else:
                print("Неверный пункт меню!")