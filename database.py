
bookshelf = []


def add_book(name, author):
    bookshelf.append({'name':name, 'author':author, 'read':False})


def get_all_books():
    return bookshelf

def mark_book_as_read(name):
    for book in bookshelf:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    global bookshelf
    bookshelf_temp = [book for book in bookshelf if book['name'] != name]
    bookshelf = bookshelf_temp