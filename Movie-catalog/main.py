from utils import database

UserChoise = """
Enter:
- a - add new book.
- l - list all books.
- r - mark book as read.
- d - delete a book.
- q - to quit the program.

Your choise: """


def prompt_add_book():
    author = input("Please enter book author: ")
    name = input("Please enter book name: ")

    database.add_book(name, author)


def list_all_books():
    books = database.get_all_books()
    for book in books:
        print (f"{book['name']} by {book['author']}, read: {book['read']}")

def prompt_read_book():
    name = input("Please enter name of the book you have just finished reading: ")

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Please enter name of the book you want to delete: ")
    database.delete_book(name)


def menu():
        user_input = input(UserChoise)

        while user_input != 'q':
            if user_input == 'a':
                prompt_add_book()
            elif user_input == 'l':
                list_all_books()
            elif user_input == 'r':
                prompt_read_book()
            elif user_input == 'd':
                prompt_delete_book()
            else:
                print ("Wrong Command! Please try again!")

            user_input = input(UserChoise)


menu()