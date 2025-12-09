from src.library import Book

def test_book_created_available():
    b = Book("Title", "Author", 2020)
    assert b.is_available() is True

def test_mark_as_taken_and_returned():
    b = Book("Title", "Author", 2020)
    b.mark_as_taken()
    assert b.is_available() is False
    b.mark_as_returned()
    assert b.is_available() is True
