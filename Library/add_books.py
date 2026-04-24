from utils import books

def add_book(name):
    if name not in books:
        books[name] = "Available"
        return True
    return False