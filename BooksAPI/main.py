# ! This code creates a API to get data from a Books DB -personal DB-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .client import MONGO_URL
# ? Import the FastAPI librarys to create the views and manage the CORS
# ? Import the pymongo client and serverAPI to connect to the database

# ! Start the App with FastAPI
app = FastAPI()

# ? create a client to comunicate to the db
client = MongoClient(MONGO_URL, server_api=ServerApi('1'))

# ! Allows CORS from all
origins = ["*"]

# ? Set the CORS Deatils
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ! Views Section

# ? This function returns my books wishlist.
# * Create an empty list to store the books in the wishlist.
# * Iterate through all the books in the library.
# * Add the book to the wishlist.
# * Return the wishlist.


@app.get("/wishlist")
async def root():

    wishlist = []

    for book in client.Library.Books.find({"wishList": True}):
        wishlist.append({"name": book['name'], "author": book['author']})

    return wishlist

# ? This function returns my library.
# * Create an empty list to store the books in the library.
# * Iterate through all the books in the library.
# * Add the book to the library, along with the book's read status.
# * Return the library.


@app.get("/library")
async def root():

    library = []

    for book in client.Library.Books.find({"wishList": False}):
        library.append(
            {"name": book['name'], "author": book['author'], "isReaded": book['readed']})

    return library

# ! view not used currently
# ? This function returns all the books by the specified author.
# * Create an empty list to store the books.
# * Iterate through all the books in the library.
# * Add the book to the list.
# * Return the list of books.


@app.get("/books/{author}")
async def root(author: str):

    books = []

    for book in client.Library.Books.find({"author": author}):
        books.append(
            {"name": book['name'], "author": book['author'], "isReaded": book['readed']})

    return books
