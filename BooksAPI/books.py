def Book(book: dict) -> dict:
    """
        ? Convert a book dictionary to a simplified book dictionary.

        Args:
            * - book (dict): A dictionary representing a book.

        Returns:
            * - dict: A simplified book dictionary with keys 'name' and 'author'.
    """
    if not book:
        return {}
    return {
        "name": book["name"],
        "author": book["author"],
    }


def BookFull(book: dict) -> dict:
    """
        ? Convert a book dictionary to a full book dictionary.

        Args:
            * - book (dict): A dictionary representing a book.

        Returns:
            * - dict: A full book dictionary with keys 'name', 'author', 'isReaded', and 'wishList'.
    """
    if not book:
        return {}
    return {
        "name": book["name"],
        "author": book["author"],
        "isReaded": book["readed"],
        "wishList": book["wishList"],
        "favorite": book["favorite"] if "favorite" in book else False,
    }


def BookList(books: list) -> list:
    """
        ? Convert a list of book dictionaries to a list of simplified book dictionaries.

        Args:
            * - books (list): A list of dictionaries representing books.

        Returns:
            * - list: A list of simplified book dictionaries with keys 'name' and 'author'.
    """
    return [Book(book) for book in books]


def Author(book: dict) -> str:
    """
        ? Extract the author name from a book dictionary.

        Args:
            * - book (dict): A dictionary representing a book.

        Returns:
            * - str: The author's name.
    """
    return book["author"]


def Authors(books: list) -> list:
    """
        ? Extract a list of unique author names from a list of book dictionaries.

        Args:
            * - books (list): A list of dictionaries representing books.

        Returns:
            * - list: A list of unique author names.
    """
    return sorted(list(set([Author(book) for book in books])))


def BookFullList(books: list) -> list:
    return [BookFull(book) for book in books]
