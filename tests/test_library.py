import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.library import (
    Book,
    PrintedBook,
    User,
    Librarian,
    Library,
)
def test_book_initially_available():
    book = Book("Тестовая книга", "Автор", 2020)
    assert book.is_available() is True


def test_book_mark_as_taken_and_returned():
    book = Book("Тестовая книга", "Автор", 2020)
    book.mark_as_taken()
    assert book.is_available() is False
    book.mark_as_returned()
    assert book.is_available() is True


def test_printed_book_repair_changes_condition_in_str():
    book = PrintedBook("Книга", "Автор", 2000, 100, "плохая")
    book.repair()
    text = str(book)
    assert "Cостояние: хорошая" in text


def test_library_lend_and_return_flow():
    library = Library()
    user = User("Анна")
    book = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")

    library.add_book(book)
    library.add_user(user)

    # выдача книги
    result_lend = library.lend_book("Война и мир", "Анна")
    assert result_lend is True
    assert book.is_available() is False
    assert book in user.get_borrowed_books()

    # возврат книги
    result_return = library.return_book("Война и мир", "Анна")
    assert result_return is True
    assert book.is_available() is True
    assert book not in user.get_borrowed_books()


def test_librarian_add_book_and_register_user():
    library = Library()
    librarian = Librarian("Мария")
    user = User("Анна")
    book = PrintedBook("Книга", "Автор", 2000, 300, "хорошая")

    librarian.add_book(library, book)
    librarian.register_user(library, user)

    # проверяем, что книгу можно найти и выдать этому пользователю
    assert library.find_book("Книга") is not None
    assert library.lend_book("Книга", "Анна") is True
