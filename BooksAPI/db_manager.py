"""
    ? Database Manager for Book Library

    * This module provides functions to manage a book library stored in a MongoDB database using PyMongo.

    Requirements:
        * - PyMongo library for MongoDB access
        * - MONGO_URL: MongoDB connection URL
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from client import MONGO_URL
from books import *


# Connect to MongoDB
client = MongoClient(MONGO_URL, server_api=ServerApi('1'))


def get_books():
    """
        Retrieve a list of all books in the library.

        Returns:
            * list: A list of dictionaries, each representing a book with keys 'name' and 'author'.

        Note:
            * If no books are found, it returns a dictionary with a "message" key.
    """
    books = BookList(client.Library.Books.find().sort(
        "author", pymongo.ASCENDING))
    return books if books != [] else {"message": "No books found"}


def get_book(name: str):
    """
        Retrieve details of a specific book by its name.

        Args:
            * name (str): The name of the book to retrieve.

        Returns:
            * dict: A dictionary representing the book with keys 'name', 'author', 'readed', and 'wishList'.

        Note:
            * If the book is not found, it returns a dictionary with a "message" key.
    """
    book = BookFullList(client.Library.Books.find(
        {"name": {"$regex": f'{name}'}}).sort([("readed", pymongo.DESCENDING), ("author", pymongo.ASCENDING)]))
    return book if book != [] else {"message": "Book not found"}


def get_readed_books():
    """
        Retrieve a list of books marked as read in the library.

        Returns:
            * list: A list of dictionaries, each representing a read book with keys 'name' and 'author'.

        Note:
            * If no read books are found, it returns a dictionary with a "message" key.
    """
    books = BookFullList(client.Library.Books.find({"readed": True}).sort(
        "author", pymongo.ASCENDING))
    return books if books != [] else {"message": "No books found"}


def get_books_to_read():
    """
        Retrieve a list of books in the library that are yet to be read.

        Returns:
            * list: A list of dictionaries, each representing a book to read with keys 'name' and 'author'.

        Note:
            * If no books to read are found, it returns a dictionary with a "message" key.
    """
    books = BookFullList(client.Library.Books.find(
        {"readed": False, "wishList": False}).sort(
        "author", pymongo.ASCENDING))
    return books if books != [] else {"message": "No books found"}


def get_authors():
    """
        Retrieve a list of unique authors in the library.

        Returns:
            * list: A list of author names.

        Note:
            * If no authors are found, it returns a dictionary with a "message" key.
    """
    authors = Authors(client.Library.Books.find().sort(
        "author", pymongo.ASCENDING))
    return authors if authors != [] else {"message": "No authors found"}


def get_books_by_author(author: str):
    """
        Retrieve a list of books by a specific author.

        Args:
            * author (str): The name of the author.

        Returns:
            * list: A list of dictionaries, each representing a book by the specified author with keys 'name', 'author', and 'isReaded'.

        Note:
            * If no books by the author are found, it returns a dictionary with a "message" key.
    """
    books = BookFullList(client.Library.Books.find({"author": author}).sort(
        [("readed", pymongo.DESCENDING), ("name", pymongo.ASCENDING)]))

    return books if books != [] else {"message": "This author don't has books"}


def get_books_in_library():
    """
        Retrieve a list of books in the library (excluding wishlist books).

        Returns:
            * list: A list of dictionaries, each representing a book in the library with keys 'name', 'author', and 'isReaded'.

        Note:
            * If no books are found in the library, it returns a dictionary with a "message" key.
    """
    library = BookFullList(client.Library.Books.find(
        {"wishList": False}).sort([("readed", pymongo.DESCENDING), ("author", pymongo.ASCENDING)]))
    return library if library != [] else {"message": "No books in library"}


def get_books_in_wishlist():
    """
        Retrieve a list of books in the wishlist.

        Returns:
            * list: A list of dictionaries, each representing a book in the wishlist with keys 'name' and 'author'.

        Note:
            * If no books are found in the wishlist, it returns a dictionary with a "message" key.
    """
    wishlist = BookFullList(client.Library.Books.find({"wishList": True}).sort(
        [("author", pymongo.ASCENDING), ("name", pymongo.ASCENDING)]))
    return wishlist if wishlist != [] else {"message": "No books in wishlist"}


def create_book(book: dict):
    """
        Create a new book entry in the library.

        Args:
            * book (dict): A dictionary representing the book with keys 'name', 'author', 'readed', and 'wishList'.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book created successfully" or "Book already exists".
    """
    if get_book(book['name']) != {"message": "Book not found"}:
        return {"message": "Book already exists"}
    client.Library.Books.insert_one(book)
    return {"message": "Book created successfully"}


def delete_book(name: str):
    """
        Delete a book from the library by name.

        Args:
            * name (str): The name of the book to be deleted.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book deleted successfully" or "Book not found".
    """
    if get_book(name) != {"message": "Book not found"}:
        client.Library.Books.delete_one({"name": name})
        return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}


def out_of_wishlist(name: str):
    """
        Remove a book from the wishlist by name.

        Args:
            * name (str): The name of the book to be removed from the wishlist.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book removed from wishlist successfully" or "Book not found".
    """
    if get_book(name) != {"message": "Book not found"}:
        client.Library.Books.update_one(
            {"name": name}, {"$set": {"wishList": False}})
        return {"message": "Book removed from wishlist successfully"}
    return {"message": "Book not found"}


def add_to_favorites(name: str):
    """
        Mark a book as a favorite by name.

        Args:
            * name (str): The name of the book to be marked as a favorite.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book added to favorites successfully" or "Book not found".
    """
    if get_book(name) != {"message": "Book not ofund"}:
        client.Library.Books.update_one(
            {"name": name}, {"$set": {"favorite": True}})
        return {"message": "Book added to favorites successfully"}
    return {"message": "Book not found"}


def get_favorites():
    """
        Retrieve a list of favorite books in the library.

        Returns:
            * list: A list of dictionaries, each representing a favorite book with keys 'name' and 'author'.

        Note:
            * If no favorite books are found, it returns a dictionary with a "message" key.
    """
    books = BookFullList(client.Library.Books.find({"favorite": True}).sort(
        [("author", pymongo.ASCENDING), ("name", pymongo.ASCENDING)]))
    return books if books != [] else {"message": "No books in favorites"}


def read_a_book(name: str):
    """
        Mark a book as read by name.

        Args:
            * name (str): The name of the book to be marked as read.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book marked as read successfully" or "Book not found".
    """
    if get_book(name) != {"message": "Book not found"}:
        client.Library.Books.update_one(
            {"name": name}, {"$set": {"readed": True}})
        return {"message": "Book marked as read successfully"}
    return {"message": "Book not found"}


def unread_a_book(name: str):
    """
        Mark a book as unread by name.

        Args:
            * name (str): The name of the book to be marked as unread.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book marked as unread successfully" or "Book not found".
    """
    if get_book(name) != {"message": "Book not found"}:
        client.Library.Books.update_one(
            {"name": name}, {"$set": {"readed": False}})
        return {"message": "Book marked as unread successfully"}
    return {"message": "Book not found"}


def unfavorite_a_book(name: str):
    """
        Remove a book from the favorites by name.

        Args:
            * name (str): The name of the book to be removed from the favorites.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book removed from favorites successfully" or "Book not found".
    """
    if get_book(name) != {"message": "Book not found"}:
        client.Library.Books.update_one(
            {"name": name}, {"$set": {"favorite": False}})
        return {"message": "Book removed from favorites successfully"}
    return {"message": "Book not found"}


def into_wishlist_a_book(name: str):
    if get_book(name) != {"message": "Book not found"}:
        client.Library.Books.find_one_and_update(
            {"$and": [{"name": name}, {"readed": False}]}, {"$set": {"wishList": True}})
        return {"message": "Book added to wishlist successfully"}
    return {"message": "Book not found"}
