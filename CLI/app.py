import os
import sys


class Library:
    """
        * The Library class provides a command-line interface for interacting with a book library using the 'db_manager'.
        * It allows users to perform various operations on books such as retrieval, creation, deletion, and more.
    """
    """
        * This is important because we need the db_manager
        * Allow to import the db_manager without errors
    """
    db_manager = None
    sys.path.append("../BooksAPI")
    import db_manager
    db_manager = db_manager

    @classmethod
    def get_book_name(cls) -> str:
        """
            ? Prompt the user to enter a book name and return it as a string.

            Returns:
                * - str: The book name entered by the user.
        """
        name = input("Enter book name: ")
        return name

    @classmethod
    def create_book_dict(cls) -> dict:
        """
            ? Prompt the user to enter book details and return them as a dictionary.

            Returns:
                * - dict: A dictionary containing book details including name, author, readed, and wishList.
        """
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
        """
            ? Display a list of books or a message to the console.

            Args:
                * - books (list | dict): Either a list of books or a dictionary containing a message.

            Notes:
                * - If 'message' is present in the dictionary, it will print the message.
                * - If the input is a dictionary, it will be converted to a list for printing if needed.
        """
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
        """
            * Retrieve and print a list of all books in the library.
        """
        books = cls.db_manager.get_books()
        Library.print_books(books)

    @classmethod
    def get_book(cls):
        """
            * Retrieve and print a book by name.
        """
        name = Library.get_book_name()
        books = cls.db_manager.get_book(name)
        Library.print_books(books)

    @classmethod
    def get_readed_books(cls):
        """
            * Retrieve and print a list of readed books.
        """
        books = cls.db_manager.get_readed_books()
        Library.print_books(books)

    @classmethod
    def get_books_to_read(cls):
        """
            * Retrieve and print a list of books to read (unreaded books).
        """
        books = cls.db_manager.get_books_to_read()
        Library.print_books(books)

    @classmethod
    def get_authors(cls):
        """
            * Retrieve and print a list of unique authors from the library.
        """
        books = cls.db_manager.get_authors()
        Library.print_books(books)

    @classmethod
    def get_books_in_library(cls):
        """
            * Retrieve and print a list of books in the library (excluding wishlist books).
        """
        books = cls.db_manager.get_books_in_library()
        Library.print_books(books)

    @classmethod
    def get_books_in_wishlist(cls):
        """
            * Retrieve and print a list of books in the wishlist.
        """
        books = cls.db_manager.get_books_in_wishlist()
        Library.print_books(books)

    @classmethod
    def get_favorites(cls):
        """
            * Retrieve and print a list of favorite books.
        """
        books = cls.db_manager.get_favorites()
        Library.print_books(books)

    @classmethod
    def get_books_by_author(cls):
        """
            * Prompt the user to enter an author's name, then retrieve and print books by that author.
        """
        author = input("Enter author name: ")
        books = cls.db_manager.get_books_by_author(author)
        Library.print_books(books)

    @classmethod
    def create_book(cls):
        """
            * Prompt the user to enter book details, create a new book entry, and print the result.
        """
        book = Library.create_book_dict()
        result = cls.db_manager.create_book(book)
        Library.print_books(result)

    @classmethod
    def delete_book(cls):
        """
            * Prompt the user to enter a book name, delete the book, and print the result.
        """
        name = Library.get_book_name()
        result = cls.db_manager.delete_book(name)
        Library.print_books(result)

    @classmethod
    def read_book(cls):
        """
            * Prompt the user to enter a book name, mark the book as read, and print the result.
        """
        name = Library.get_book_name()
        result = cls.db_manager.read_a_book(name)
        Library.print_books(result)

    @classmethod
    def book_out_of_wishlist(cls):
        """
            * Prompt the user to enter a book name, remove the book from the wishlist, and print the result.
        """
        name = Library.get_book_name()
        result = cls.db_manager.out_of_wishlist(name)
        Library.print_books(result)

    @classmethod
    def add_book_to_favorites(cls):
        """
            * Prompt the user to enter a book name, mark the book as a favorite, and print the result.
        """
        name = Library.get_book_name()
        result = cls.db_manager.add_to_favorites(name)
        Library.print_books(result)


class CLI:
    """
        ? Command Line Interface (CLI) for interacting with the book library.

        * This class provides a command-line interface to perform various operations on a book library.
        * It includes methods for displaying a menu, receiving user commands, and executing operations.

        Methods:
            * - clear_screen: Clears the terminal screen.
            * - show_menu: Displays the available commands in the menu.
            * - get_command: Prompts the user for a command and returns it as a string.
            * - execute: Runs the CLI interface and processes user commands to interact with the library.

        Example Usage:
            To use the CLI, create an instance of the `CLI` class and call the `execute` method to start the interaction.
    """

    @classmethod
    def clear_screen(cls):
        """
            ? Clears the terminal screen.

            * This method detects the operating system and uses the appropriate command to clear the screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def show_menu(cls):
        """
            ? Displays the available commands in the menu.

            * This method prints a list of available commands that the user can enter to interact with the library.
        """
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
        """
            ? Prompts the user for a command and returns it as a string.

            Returns:
                * - str: The user-entered command.
        """
        command = input("Enter command: ")
        return command.strip()

    @classmethod
    def execute(cls):
        """
            ? Runs the CLI interface and processes user commands to interact with the library.

            * This method continuously prompts the user for commands and executes the corresponding library operations.
            * It provides an interactive way to manage the book library based on user input.
        """
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
    """
        * main function to execute the program calling CLI and the method execute
    """
    CLI.execute()


if __name__ == "__main__":
    main()
