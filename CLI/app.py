import os
import sys


class Library:
    db_manager = None
    sys.path.append("../BooksAPI")
    import db_manager
    db_manager = db_manager

    @classmethod
    def get_book_name(cls) -> str:
        name = input("Enter book name: ")
        return name

    @classmethod
    def create_book_dict(cls) -> dict:
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        readed = input("Is readed (y/n): ")
        if readed == "y" or readed == "Y":
            wishlist = "n"
        else:
            wishlist = input("Is in wishlist (y/n): ")
        return {"name": name, "author": author, "readed": True if readed == "y" or readed == "Y" else False, "wishList": True if wishlist == "y" or wishlist == "Y" else False}

    @classmethod
    def print_books(cls, books: list | dict):
        if 'message' in books:
            print(books["message"])
        else:
            if type(books) == dict:
                books = [books]
            for book in books:
                if type(book) == dict:
                    book = f"{book['name']} - {book['author']} - {'readed' if book['isReaded']==True else 'unreaded'}" if 'isReaded' in book else f"{book['name']} - {book['author']}"
                    print(book)
                else:
                    print(book)

    @classmethod
    def get_books(cls):
        books = cls.db_manager.get_books()
        Library.print_books(books)

    @classmethod
    def get_book(cls):
        name = Library.get_book_name()
        books = cls.db_manager.get_book(name)
        Library.print_books(books)

    @classmethod
    def get_readed_books(cls):
        books = cls.db_manager.get_readed_books()
        Library.print_books(books)

    @classmethod
    def get_books_to_read(cls):
        books = cls.db_manager.get_books_to_read()
        Library.print_books(books)

    @classmethod
    def get_authors(cls):
        books = cls.db_manager.get_authors()
        Library.print_books(books)

    @classmethod
    def get_books_in_library(cls):
        books = cls.db_manager.get_books_in_library()
        Library.print_books(books)

    @classmethod
    def get_books_in_wishlist(cls):
        books = cls.db_manager.get_books_in_wishlist()
        Library.print_books(books)

    @classmethod
    def get_favorites(cls):
        books = cls.db_manager.get_favorites()
        Library.print_books(books)

    @classmethod
    def get_books_by_author(cls):
        author = input("Enter author name: ")
        books = cls.db_manager.get_books_by_author(author)
        Library.print_books(books)

    @classmethod
    def create_book(cls):
        book = Library.create_book_dict()
        result = cls.db_manager.create_book(book)
        Library.print_books(result)

    @classmethod
    def delete_book(cls):
        name = Library.get_book_name()
        result = cls.db_manager.delete_book(name)
        Library.print_books(result)

    @classmethod
    def read_book(cls):
        name = Library.get_book_name()
        result = cls.db_manager.read_a_book(name)
        Library.print_books(result)

    @classmethod
    def book_out_of_wishlist(cls):
        name = Library.get_book_name()
        result = cls.db_manager.out_of_wishlist(name)
        Library.print_books(result)

    @classmethod
    def add_book_to_favorites(cls):
        name = Library.get_book_name()
        result = cls.db_manager.add_to_favorites(name)
        Library.print_books(result)


class CLI:

    @classmethod
    def clear_screen(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def show_menu(cls):
        print("Commands:")
        print("--------------------")
        print("all - show all books")
        print("one - find book")
        print("wishlist - show wishlist")
        print("library - show library")
        print("readed - readed books")
        print("unread - unreaded books")
        print("authors - show authors")
        print('favorites - view favorites')
        print("by author - show books by author")
        print("out wishlist - out of wishlist")
        print('favorite - add book to favorites')
        print("read - read book")
        print("delete - delete book")
        print("add - add book")
        print("exit - exit")
        print("--------------------\n")

    @classmethod
    def get_command(cls) -> str:
        command = input("Enter command: ")
        return command.strip()

    @classmethod
    def execute(cls):
        while True:
            input()
            cls.clear_screen()
            cls.show_menu()
            command: str = cls.get_command()

            if command == "exit":
                sys.exit()
            elif command == "all":
                Library.get_books()
                continue
            elif command == "one":
                Library.get_book()
                continue
            elif command == "wishlist":
                Library.get_books_in_wishlist()
                continue
            elif command == "library":
                Library.get_books_in_library()
                continue
            elif command == "readed":
                Library.get_readed_books()
                continue
            elif command == "unread":
                Library.get_books_to_read()
                continue
            elif command == "authors":
                Library.get_authors()
                continue
            elif command == "favorites":
                Library.get_favorites()
                continue
            elif command == "by author":
                Library.get_books_by_author()
                continue
            elif command == "out wishlist":
                Library.book_out_of_wishlist()
                continue
            elif command == "favorite":
                Library.add_book_to_favorites()
                continue
            elif command == "read":
                Library.read_book()
                continue
            elif command == "delete":
                Library.delete_book()
                continue
            elif command == "add":
                Library.create_book()
                continue
            else:
                print("Command not found")
                continue


def main():
    CLI.execute()


if __name__ == "__main__":
    main()
