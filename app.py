from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from BooksAPI.client import MONGO_URL
# ? import the pymongo client and serverAPI to connect to the database
import os
# ? import os to manipulate the terminal

# ? create a client to comunicate to the db
client = MongoClient(MONGO_URL, server_api=ServerApi('1'))

# ? Insert Book to the db
# * This function inserts a book into the database.
# * Args:
# *   -name: The name of the book.
# *   -author: The author of the book.
# *   -readed: Whether the book has been read.
# *   -wishlist: Whether the book is on the wishlist.
# * Check if the book already exists in the database.
# * If not exist insert the book into the database.


def insertBook(name, author, readed, wishlist):

    if client.Library.Books.find_one({"name": name}) is not None:
        print("Book already exists!")

    else:
        client.Library.Books.insert_one(
            {'name': name, "author": author, "readed": readed, 'wishList': wishlist})

# ? Show all book titles in the library
# * This function prints all the book titles in the library, grouped by read status and wishlist status.
# * Clear the screen.
# * Get the total number of books in the library.
# * Get the number of books that are not on the wishlist.
# * Print the read books.
# * Print the unread books.
# * Print the books in the wishlist.


def showTitles():
    os.system('cls')

    c = client.Library.Books.count_documents({})

    print(f"There Are {c} Books In Library:\n")

    counter = client.Library.Books.count_documents({'wishList': False})
    bookList = []

    print(f"There Are {counter} Books In Library:")
    print("====================")
    print("\nReaded Books:")
    print("====================")

    for book in client.Library.Books.find({
            "readed": True, 'wishList': False}):

        print(book['name']+" - "+book['author'])

    print("-----------------------")
    print("\nUnreaded Books:")
    print("====================")

    for book in client.Library.Books.find({
            "readed": False, 'wishList': False}):

        print(book['name']+" - "+book['author'])

    print("-----------------------")

    counter2 = client.Library.Books.count_documents({'wishList': True})
    print(f"\nThere Are {counter2} Books In Wishlist:")
    print("====================")

    for book in client.Library.Books.find({'readed': False, 'wishList': True}):
        print(book['name']+" - "+book['author'])

# ? Find a book in the library
# * This function finds a book in the library and prints it out.
# * Args:
# * -name: The name of the book.
# * Clear the screen.
# * Find the book in the database.
# * If the book is not found, print an error message.
# * Otherwise, print the book information.


def findBook(name):

    os.system('cls')

    book = client.Library.Books.find_one({"name": name})

    if book is None:
        print("Book not found")

    elif book['wishList']:
        print("Book is in your wishlist:")
        print("====================")
        print(book['name']+" - "+book['author'])

    else:
        print("Book is in your library:")
        print("====================")
        print(book['name']+" - "+book['author'])

# ? Print all read books in the library
# * This function prints all the read books in the library.
# * Clear the screen.
# * Find all the read books.
# * Print the book information.


def onlyReaded():

    os.system('cls')

    print("Readed Books:")
    print("====================")

    for book in client.Library.Books.find({"readed": True}):
        print(book['name']+" - "+book['author'])

# ? Print all books to read in the library
# * This function prints all the books that are not read and not in the wishlist.
# * Clear the screen.
# * Find all the books that are not read and not in the wishlist.
# * Print the book information.


def toRead():

    os.system('cls')

    print("To Read Books:")
    print("====================")

    for book in client.Library.Books.find({"readed": False, 'wishList': False}):
        print(book['name']+" - "+book['author'])

# ? Mark a book as read
# * This function marks a book as read in the library.
# * Args:
#  * -name: The name of the book.
# * Clear the screen.
# * Find the book in the database.
# * If the book is not found, print an error message.
# * Otherwise, mark the book as read.


def Readed(name):

    os.system('cls')

    client.Library.Books.find_one_and_update(
        {"name": name}, {"$set": {"readed": True}})

    print("readed!")

# ? Find books by author
# * This function finds all the books by a given author in the library.
# * Args:
# * -author: The name of the author.
# * Clear the screen.
# * Find all the books by the author in the library.
# * Print the book information.
# * Find all the books by the author in the wishlist.
# * Print the book information.


def byAuthor(author):

    os.system('cls')

    print(f'Books from {author} in your.Library:')
    print("====================")

    for book in client.Library.Books.find({"author": author, 'wishList': False}):
        print(book['name']+" - "+book['author'])

    print(f'\nBooks from {author} in your wishlist:')
    print("====================")

    for book in client.Library.Books.find({"author": author, 'wishList': True}):
        print(book['name']+" - "+book['author'])

# ? Delete a book
# * This function deletes a book from the library.
# * Args:
# * -name: name of the book.


def deleteBook(name):

    client.Library.Books.delete_one({"name": name})
    print("Deleted!")

# ? Get all authors in the library
# * This function gets all the authors in the library.
# * Clear the screen.
# * Get a list of all the authors.
# * Remove duplicates from the list of authors.
# * Print all the authors.


def authors():

    os.system('cls')

    print("Authors:")
    print("====================")

    authors = []

    for book in client.Library.Books.find():
        authors.append(book['author'])

    for author in set(authors):
        print(author)

# ? Get all books in wishlist
# * This function gets all the books in the wishlist.
# * Clear the screen.
# * Get the number of books in the wishlist.
# * Get all the books in the wishlist.
# * Print the book information.


def wishList():

    os.system('cls')

    counter = client.Library.Books.count_documents({'wishList': True})

    print(f"There Are {counter} Books In Wishlist:")
    print("====================")

    for book in client.Library.Books.find({"wishList": True}):
        print(book['name']+" - "+book['author'])


# ? Remove a book from wishlist
# * This function removes a book from the wishlist.
# * Args:
# * -name: The name of the book.
# * Clear the screen.
# * Update the book in the database to remove it from the wishlist.
# * Print a message to confirm that the book has been removed from the wishlist.

def outOfWishList(name):

    os.system('cls')

    client.Library.Books.update_one(
        {"name": name}, {"$set": {"wishList": False}})
    print("Book out of wishlist!")

# ? Add a book to favorites
# * This function adds a book to the favorites.
# * Args:
# * -name: The name of the book.
# * Clear the screen.
# * Find the book in the database.
# * If the book is found, add it to the favorites.
# * Otherwise, print a message.


def favorite(name):

    os.system('cls')

    book = client.Library.Books.find(
        {"name": name, 'readed': True, 'wishlist': False})

    if book:
        client.Library.Books.update_one(
            {"name": name}, {"$set": {"favorite": True}})
        print("Book added to favorites!")

    else:
        print("The book isn't in your library")

# ? View favorites
# * This function views the favorites.
# * Clear the screen.
# * Find all the books in the favorites.
# * Print the book information.


def viewFavorites():

    os.system('cls')

    print("Favorites:")
    print("====================")

    for book in client.Library.Books.find({"favorite": True}):
        print(book['name']+" - "+book['author'])

# ? show all commands and information of each command


def showCommands():

    print("Commands:")
    print("--------------------")
    print("show all - show all books")
    print("find - find book")
    print("only readed - show only readed books")
    print("to read - show only to read books")
    print("readed - readed book")
    print("by author - show books by author")
    print("authors - show authors")
    print("delete book - delete book")
    print("out wishlist - out of wishlist")
    print("wishlist - show wishlist")
    print('favorite - add book to favorites')
    print('view favorites - view favorites')
    print("add - add book")
    print("exit - exit")
    print("--------------------\n")

# ! This program is my simple library management system.
# ? variable to run the CLI


running = True

# * Show the list of commands.
# * Get the command.
# * Check the command and perform the corresponding action.

while running:

    input()
    os.system('cls')

    showCommands()

    command = input("Enter command: ")

    if command == "exit":
        running = False
        break

    elif command == "show all":
        showTitles()
        continue

    elif command == "find":
        findBook(input("Enter book name: "))
        continue

    elif command == "only readed":
        onlyReaded()
        continue

    elif command == "to read":
        toRead()
        continue

    elif command == "readed":
        name = input("Enter book name: ")
        Readed(name)
        continue

    elif command == "by author":
        author = input("Enter author name: ")
        byAuthor(author)
        continue

    elif command == "authors":
        authors()
        continue

    elif command == "delete book":
        name = input("Enter book name: ")
        deleteBook(name)
        continue

    elif command == "out wishlist":
        name = input("Enter book name: ")
        outOfWishList(name)
        continue

    elif command == "wishlist":
        wishList()
        continue

    elif command == "favorite":
        name = input("Enter book name: ")
        favorite(name)
        continue

    elif command == "view favorites":
        viewFavorites()
        continue

    elif command == "add":

        # * Clear the screen.
        # * Get the book name.
        # * Get the author name.
        # * Get the readed status.
        # * Get the wishlist status.
        # * Insert the book.

        os.system('cls')

        name = input("Enter book name: ")
        author = input("Enter author name: ")
        readed = input("Enter if readed(y/n): ")
        wishlist = True

        if readed == "y":
            readed = True
            wishlist = False

        else:

            readed = False
            wishlist = input("Enter if wishlist(y/n): ")

            if wishlist == "y":
                wishlist = True

            else:
                wishlist = False

        insertBook(name, author, readed, wishlist)
        continue

    else:
        print("Please Enter Valid Command!")
        continue
