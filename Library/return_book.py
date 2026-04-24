from utils import issued_book
from utils import books

def return_book(book_name):
    book_name = book_name.strip().title()
    if book_name in issued_book:
        issued_book.pop(book_name)
        books[book_name] = "Available"
        return True
    return False
