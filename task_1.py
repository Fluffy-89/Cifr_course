from datetime import datetime


class Vehicle:
    """
    Класс, представляющий транспортное средство.

    Attributes:
        make (str): Производитель транспортного средства.
        series (str): Модельный ряд.
        production_year (int): Год выпуска.
    """

    def __init__(self, make: str, series: str, production_year: int):
        if production_year < 1886 or production_year > 2025:
            raise ValueError("Год выпуска должен быть в диапазоне 1886-2025.")
        self.make = make
        self.series = series
        self.production_year = production_year

    def calculate_age(self) -> int:
        """
        Вычисляет возраст транспортного средства.

        Returns:
            int: Возраст в годах.

        Пример:
        >>> vehicle = Vehicle('Honda', 'Accord', 2018)
        >>> vehicle.calculate_age()  # Если сейчас 2025 год, вернёт 7
        7
        """
        current_year = datetime.now().year
        return current_year - self.production_year

    def activate(self) -> str:
        """
        Активирует транспортное средство.

        Returns:
            str: Сообщение об активации.

        >>> vehicle = Vehicle('BMW', 'X5', 2022)
        >>> vehicle.activate()
        'Транспортное средство BMW X5 активировано.'
        """
        return f'Транспортное средство {self.make} {self.series} активировано.'


class Literature:
    """
    Класс, представляющий литературное произведение.

    Attributes:
        name (str): Название произведения.
        writer (str): Автор произведения.
        page_count (int): Количество страниц.
    """

    def __init__(self, name: str, writer: str, page_count: int):
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self.name = name
        self.writer = writer
        self.page_count = page_count

    def consume(self, pages_consumed: int) -> str:
        """
        Читает указанное количество страниц.

        Args:
            pages_consumed (int): Прочитанные страницы.

        Returns:
            str: Сообщение о прогрессе чтения.

        >>> novel = Literature('Война и мир', 'Лев Толстой', 1225)
        >>> novel.consume(100)
        'Прочитано 100 страниц из произведения "Война и мир".'
        """
        if pages_consumed <= 0:
            raise ValueError("Количество страниц должно быть положительным.")

        return f'Прочитано {pages_consumed} страниц из произведения "{self.name}".'

    def describe(self) -> str:
        """
        Возвращает описание произведения.

        Returns:
            str: Информация о произведении.

        >>> story = Literature('Преступление и наказание', 'Достоевский', 672)
        >>> story.describe()
        'Произведение "Преступление и наказание" создано Достоевский и состоит из 672 страниц.'
        """
        return f'Произведение "{self.name}" создано {self.writer} и состоит из {self.page_count} страниц.'


class Plant:
    """
    Класс, представляющий растение.

    Attributes:
        variety (str): Разновидность растения.
        size (float): Высота в метрах.
    """

    def __init__(self, variety: str, size: float):
        if size < 0:
            raise ValueError("Высота растения не может быть отрицательной.")
        self.variety = variety
        self.size = size

    def develop(self, growth: float = 0.5) -> None:
        """
        Увеличивает размер растения.

        Args:
            growth (float): Прирост в метрах. По умолчанию 0.5.

        >>> oak = Plant('Дуб', 3.5)
        >>> oak.develop(1.2)
        >>> oak.size
        4.7
        """
        if growth < 0:
            raise ValueError("Прирост не может быть отрицательным.")

        self.size += growth

    def get_description(self) -> str:
        """
        Возвращает описание растения.

        Returns:
            str: Информация о растении.

        >>> pine = Plant('Сосна', 8.2)
        >>> pine.get_description()
        'Растение разновидности Сосна имеет высоту 8.2 метров.'
        """
        return f'Растение разновидности {self.variety} имеет высоту {self.size} метров.'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

