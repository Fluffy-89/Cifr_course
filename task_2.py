from task_1 import BOOK_DATA, LiteraryWork


class BookCollection:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def calculate_next_id(self):
        return 1 if not self.items else max(item.work_id for item in self.items) + 1

    def find_item_position(self, target_id):
        for position, item in enumerate(self.items):
            if item.work_id == target_id:
                return position
        raise ValueError("Литературное произведение с указанным идентификатором не найдено")


if __name__ == '__main__':
    # Тестирование пустой коллекции
    empty_collection = BookCollection()
    print(f"Следующий доступный ID: {empty_collection.calculate_next_id()}")

    # Создание и тестирование заполненной коллекции
    collection_items = [
        LiteraryWork(work_id=item["book_id"], title=item["title"], page_count=item["page_count"])
        for item in BOOK_DATA
    ]
    filled_collection = BookCollection(items=collection_items)

    print(f"Следующий доступный ID: {filled_collection.calculate_next_id()}")
    print(f"Позиция произведения с ID 1: {filled_collection.find_item_position(1)}")
