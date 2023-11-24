"""
    ? This module defines a FastAPI application for managing a library of books and interacts with a MongoDB database using `db_manager`.
    
    *It also includes Pydantic models for book representation.

    Modules:
        * - `FastAPI`: A modern, fast web framework for building APIs with Python.
        * - `CORSMiddleware`: Middleware for enabling Cross-Origin Resource Sharing (CORS) in the application.
        * - `db_manager`: A module for managing database operations with MongoDB.
        * - `BaseModel`: Pydantic's base model class for creating data models.
        * - `urllib.parse`: A module for parsing and handling URLs.

    Main Components:
        * - `FastAPI` application with various endpoints for managing the library of books.
        * - Pydantic `BaseModel` class for representing book data.
"""
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
import db_manager
from pydantic import BaseModel
import urllib.parse
from client import description, get_allowed_origins
from starlette.responses import RedirectResponse
from fastapi import status, HTTPException

""" 
    ? Configure the app and the CORS
"""
app = FastAPI(title="BookShell", description=description,
              summary="Personal library management API.", version="0.0.1",)

origins = get_allowed_origins()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Book(BaseModel):
    """
        Represents a book in the library.

        Attributes:
            * name (str): The name of the book.
            * author (str): The name of the book's author.
            * readed (bool, optional): Indicates whether the book has been read. Default is False.
            * wishList (bool, optional): Indicates whether the book is in the wish list. Default is True.
            * favorite (bool, optional): Indicates whether the book is marked as a favorite. It can be None if not specified.

        Note:
            * - The `readed`, `wishList`, and `favorite` attributes are optional and have default values.
            * - Use this model for creating, updating, and representing book entries in the library.
    """
    name: str
    author: str
    readed: bool = False
    wishList: bool = True
    favorite: bool = False


@app.get("/", tags=["Default"], status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def root():
    """
        Redirects to the documentation.
    """
    return RedirectResponse(url="/docs")


@app.get("/books", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of all books in the library.

        Returns:
            * List[dict]: A list of dictionaries, each representing a book with keys 'name' and 'author'.
    """
    books = db_manager.get_books()
    if "message" in books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@app.get("/books/wishlist", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of books in the wishlist.

        Returns: 
            * List[dict]: A list of dictionaries, each representing a book in the wishlist with keys 'name' and 'author'.
    """
    books = db_manager.get_books_in_wishlist()
    if "message" in books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@app.get("/books/library", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of books in the library (excluding wishlist books).

        Returns:
            * List[dict]: A list of dictionaries, each representing a book in the library with keys 'name', 'author', and 'isReaded'.
    """
    books = db_manager.get_books_in_library()
    if "message" in books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@app.get("/books/readed", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of readed books.

        Returns:
            * List[dict]: A list of dictionaries, each representing a readed book with keys 'name' and 'author'.
    """
    books = db_manager.get_readed_books()
    if "message" in books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@app.get("/books/unreaded", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of books to read (unreaded books).

        Returns:
            * List[dict]: A list of dictionaries, each representing an unreaded book with keys 'name' and 'author'.
    """
    books = db_manager.get_books_to_read()
    if "message" in books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@app.get("/books/authors", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of unique authors from the library.

        Returns:
            * List[str]: A list of unique author names.
    """
    authors = db_manager.get_authors()
    if "message" in authors:
        raise HTTPException(status_code=404, detail="No authors found")
    return authors


@app.get("/books/favorites", tags=["Library"], status_code=status.HTTP_200_OK)
def root():
    """
        Retrieve a list of favorite books.

        Returns:
            * List[dict]: A list of dictionaries, each representing a favorite book with keys 'name' and 'author'.
    """
    books = db_manager.get_favorites()
    if "message" in books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@app.get("/books/{name}", tags=["Library"], status_code=status.HTTP_200_OK)
def root(name: str):
    """
        Retrieve a book by name.

        Args:
            * name (str): The name of the book to retrieve.

        Returns:
            * dict: A dictionary representing the book with keys 'name', 'author', 'readed', 'wishList', and 'favorite'.
    """
    name = urllib.parse.unquote(name)
    book = db_manager.get_book(name)
    if "message" in book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/books/author/{author}", tags=["Library"], status_code=status.HTTP_200_OK)
def root(author: str):
    """
        Retrieve a list of books by a specific author.

        Args:
            * author (str): The name of the author.

        Returns:
            * List[dict]: A list of dictionaries, each representing a book by the specified author with keys 'name', 'author', and 'isReaded'.
    """
    books = db_manager.get_books_by_author(author)
    if "message" in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No books found by this author"
        )
    return books


@app.post("/books", tags=["Library"], status_code=status.HTTP_201_CREATED)
def root(book: Book):
    """
        Create a new book entry in the library.

        Args:
            * book (Book): A Pydantic model representing the book.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book created successfully" or "Book already exists".
    """
    result = db_manager.create_book(book.dict())
    return result


@app.delete("/books/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    """
        Delete a book from the library by name.

        Args:
            * name (str): The name of the book to be deleted.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book deleted successfully" or "Book not found".
    """
    result = db_manager.delete_book(name)
    return result


@app.put("/books/wishlist/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    """
        Remove a book from the wishlist by name.

        Args:
            * name (str): The name of the book to be removed from the wishlist.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book removed from wishlist successfully" or "Book not found".
    """
    result = db_manager.out_of_wishlist(name)
    return result


@app.put("/books/favorites/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    """
        Mark a book as a favorite by name.

        Args:
            * name (str): The name of the book to be marked as a favorite.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book added to favorites successfully" or "Book not found".
    """
    result = db_manager.add_to_favorites(name)
    return result


@app.put("/books/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    """
        Mark a book as readed by name.

        Args:
            * name (str): The name of the book to be marked as readed.

        Returns:
            * dict: A message indicating the result of the operation, e.g., "Book marked as readed successfully" or "Book not found".
    """
    result = db_manager.read_a_book(name)
    return result


@app.put("/books/unread/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    return db_manager.unread_a_book(name)


@app.put("/books/unfavorite/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    return db_manager.unfavorite_a_book(name)


@app.put("/books/intowishlist/{name}", tags=["Library"], status_code=status.HTTP_202_ACCEPTED)
def root(name: str):
    return db_manager.into_wishlist_a_book(name)
