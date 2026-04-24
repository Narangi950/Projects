from utils import issued_book
from utils import books

def issued_books(book_name):
    if book_name in books:
        status = books.pop(book_name)
        issued_book[book_name] = "Currently book having a User"
        return True
    return False