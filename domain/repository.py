class Repository:
    def get_text(self, source):
        raise NotImplementedError(
            "Метод должен быть реализован в дочернем классе"
        )

    def get_text_from_url(self, url):
        raise NotImplementedError(
            "Метод должен быть реализован в дочернем классе"
        )