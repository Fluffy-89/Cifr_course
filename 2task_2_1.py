from task_1 import Vehicle, Literature, Plant

if __name__ == "__main__":
    # Создаем экземпляры классов
    my_vehicle = Vehicle("Ford", "Focus", 2019)
    my_book = Literature("Мастер и Маргарита", "Михаил Булгаков", 384)
    my_plant = Plant("Береза", 2.8)

    # Проверяем обработку неверных аргументов
    try:
        print(my_vehicle.activate(2023))  # Лишний аргумент
    except TypeError:
        print('Ошибка: метод activate не принимает аргументов')

    try:
        print(my_book.consume([10]))  # Неправильный тип аргумента
    except TypeError:
        print('Ошибка: метод consume требует целое число')

    try:
        print(my_plant.develop("два"))  # Неправильный тип аргумента
    except TypeError:
        print('Ошибка: метод develop требует числовое значение')

    # Демонстрация корректной работы
    print("\nКорректные вызовы методов:")
    print(my_vehicle.activate())
    print(my_book.consume(50))
    my_plant.develop(0.3)
    print(my_plant.get_description())
