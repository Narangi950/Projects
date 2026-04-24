from add_books import add_book
from show_book import show_book
from issue_books import issued_books
from return_book import return_book

def library():
    while True:
        print("*"*50)
        print("\n1.add_books")
        print("2.show_books")
        print("3.issue_books")
        print("4.return_books")
        print("5.exit")
        print("*"*50)

        choice = int(input("enter the choice:" ))
        if choice == 1:
            while True:
                name_book = input("Enter a Book Title: ").strip().title()
                added = add_book(name_book)
                if added:
                    print("Successfully added your Book..")
                else:
                    print("Book is already added in your record")
                asking = input("Do you want to add more Books Yes/No: ").capitalize()
                if asking == "Yes":
                    continue
                elif asking == "No":
                    break
                else:
                    print("Invaild Input")
                    break

        elif choice == 2:
            all_books = show_book()
            if not all_books:
                print("No book are available..")
            else:
                for title,status in all_books.items():
                    print(f"Book:{title}, Status:{status}")
        elif choice == 3:
            title = input("Enter the book you want to issue: ").strip().title()
            if issued_books(title):
                print(f"Issued book :{title}")
            else:
                print("Book is not in libaray")

        elif choice == 4:
            return_book_name = input("Enter the name of the book to return: ")
            if return_book(return_book_name):
                print(f"{return_book_name} Book has been returned")
            else:
                print("Book is not issued.")
        elif choice == 5:
            print("thank you")
            break
        else:
            print("invalid choice")
            break
library()