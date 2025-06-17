class Transport:
    """Базовый класс для всех видов транспорта."""

    def __init__(self, manufacturer: str, model_name: str, production_year: int):
        self._manufacturer = manufacturer
        self._model_name = model_name
        self._production_year = production_year

    @property
    def manufacturer(self) -> str:
        """Производитель транспортного средства."""
        return self._manufacturer

    @property
    def model_name(self) -> str:
        """Модель транспортного средства."""
        return self._model_name

    @property
    def production_year(self) -> int:
        """Год выпуска транспортного средства."""
        return self._production_year

    def get_details(self) -> str:
        """Возвращает основные характеристики транспорта."""
        return f"{self.production_year} {self.manufacturer} {self.model_name}"

    def __str__(self):
        return f"Транспортное средство: {self.get_details()}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, "
                f"model_name={self.model_name!r}, production_year={self.production_year!r})")


class PassengerCar(Transport):
    """Класс для легкового транспорта."""

    def __init__(self, manufacturer: str, model_name: str, production_year: int, door_count: int):
        super().__init__(manufacturer, model_name, production_year)
        self.door_count = door_count

    @property
    def door_count(self) -> int:
        """Количество дверей в автомобиле."""
        return self._door_count

    @door_count.setter
    def door_count(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество дверей должно быть целым числом")
        if value <= 0:
            raise ValueError("Автомобиль должен иметь хотя бы одну дверь")
        self._door_count = value

    def get_details(self) -> str:
        """Возвращает полную информацию о легковом транспорте."""
        return f"{super().get_details()} | Количество дверей: {self.door_count}"

    def __str__(self):
        return f"Легковой транспорт: {self.get_details()}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, "
                f"model_name={self.model_name!r}, production_year={self.production_year!r}, "
                f"door_count={self.door_count!r})")


class CargoTransport(Transport):
    """Класс для грузового транспорта."""

    def __init__(self, manufacturer: str, model_name: str, production_year: int, max_load: float):
        super().__init__(manufacturer, model_name, production_year)
        self.max_load = max_load

    @property
    def max_load(self) -> float:
        """Максимальная грузоподъемность в тоннах."""
        return self._max_load

    @max_load.setter
    def max_load(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Грузоподъемность должна быть числом")
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть положительной")
        self._max_load = float(value)

    def get_details(self) -> str:
        """Возвращает полную информацию о грузовом транспорте."""
        return f"{super().get_details()} | Грузоподъемность: {self.max_load} т"

    def __str__(self):
        return f"Грузовой транспорт: {self.get_details()}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(manufacturer={self.manufacturer!r}, "
                f"model_name={self.model_name!r}, production_year={self.production_year!r}, "
                f"max_load={self.max_load!r})")


if __name__ == "__main__":
    # Пример использования
    sedan = PassengerCar("Toyota", "Camry", 2020, 4)
    truck = CargoTransport("Volvo", "FH", 2019, 18.0)

    print(sedan)  # Легковой транспорт: 2020 Toyota Camry | Количество дверей: 4
    print(truck)  # Грузовой транспорт: 2019 Volvo FH | Грузоподъемность: 18.0 т
