BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id=id
        self.name=name
        self.pages=pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id={self.id!r}, name={self.name!r}, pages={self.pages!r})"
from typing import Optional

from pydantic import BaseModel

# TODO написать класс Library
class Library(BaseModel):
    def __init__(self):
        books: Optional[List[Book] = []]


    def get_next_book_id(self):
        next_book_id=len(self.books)+1
        return next_book_id

    def get_index_by_book_id(self, book_id):
        index_by_book_id = 0
        for i, val in enumerate(self.books(i)):
            if self.books(i).id==book_id:
                index_by_book_id= (i+1)
            else:
                index_by_book_id+=1
        if index_by_book_id>0:
            return index_by_book_id
        else:
            raise ValueError("Книги с запрашиваемым id не существует")




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
