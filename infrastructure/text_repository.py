from urllib.request import urlopen
from urllib.error import URLError, HTTPError

from domain.repository import Repository

class TextRepository(Repository):

    def get_text(self, source):
        try:
            with open(source, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден")
        except PermissionError:
            raise PermissionError("Нет доступа к файлу")

    def get_text_from_url(self, url):
        try:
            with urlopen(url, timeout=10) as response:
                content = response.read()
                return content.decode("utf-8", errors="replace")
        except HTTPError:
            raise ValueError("Ошибка HTTP при загрузке страницы")
        except URLError:
            raise ValueError("Не удалось загрузить веб-страницу")
        except TimeoutError:
            raise ValueError("Время ожидания ответа истекло")