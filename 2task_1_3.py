class LiteraryWork:
    """Базовый класс литературного произведения."""

    def __init__(self, title: str, creator: str):
        self._title = title
        self._creator = creator

    @property
    def title(self) -> str:
        """Название произведения."""
        return self._title

    @property
    def creator(self) -> str:
        """Создатель произведения."""
        return self._creator

    def __str__(self):
        return f"Литературное произведение '{self.title}'. Создатель: {self.creator}"

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title!r}, creator={self.creator!r})"


class PrintedEdition(LiteraryWork):
    """Класс для печатных изданий."""

    def __init__(self, title: str, creator: str, page_count: int):
        super().__init__(title, creator)
        self.page_count = page_count

    @property
    def page_count(self) -> int:
        """Количество страниц в издании."""
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Издание должно содержать хотя бы одну страницу")
        self._page_count = value

    def __str__(self):
        return f"{super().__str__()} | Объём: {self.page_count} стр."

    def __repr__(self):
        return (f"{self.__class__.__name__}(title={self.title!r}, "
                f"creator={self.creator!r}, page_count={self.page_count!r})")


class AudioEdition(LiteraryWork):
    """Класс для аудиоверсий произведений."""

    def __init__(self, title: str, creator: str, length: float):
        super().__init__(title, creator)
        self.length = length

    @property
    def length(self) -> float:
        """Длительность аудиоверсии в часах."""
        return self._length

    @length.setter
    def length(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Длительность должна быть числовым значением")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._length = round(float(value), 2)

    def __str__(self):
        return f"{super().__str__()} | Длительность: {self.length} ч."

    def __repr__(self):
        return (f"{self.__class__.__name__}(title={self.title!r}, "
                f"creator={self.creator!r}, length={self.length!r})")
