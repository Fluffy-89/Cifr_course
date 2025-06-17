BOOK_DATA = [
    {
        "book_id": 1,
        "title": "test_name_1",
        "page_count": 200,
    },
    {
        "book_id": 2,
        "title": "test_name_2",
        "page_count": 400,
    }
]


class LiteraryWork:
    def __init__(self, work_id, title, page_count):
        self.work_id = work_id
        self.title = title
        self.page_count = page_count

    def display_info(self):
        return f'Произведение "{self.title}"'

    def get_details(self):
        return f"LiteraryWork(work_id={self.work_id}, title='{self.title}', page_count={self.page_count})"


if __name__ == '__main__':
    # Создаем коллекцию литературных произведений
    works_collection = [
        LiteraryWork(work_id=item["book_id"], title=item["title"], page_count=item["page_count"])
        for item in BOOK_DATA
    ]

    # Демонстрация работы методов
    for work in works_collection:
        print(work.display_info())  # Проверяем метод display_info

    print([work.get_details() for work in works_collection])  # Проверяем метод get_details
