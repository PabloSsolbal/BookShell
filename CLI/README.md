# MongoDB Python Library Management System

This Python program is a simple library management system that uses MongoDB as its database. It allows to manage books in your library, mark them as read, add them to your wishlist, and perform various other book-related operations through a CLI.

## Technologies

**Technologies Used**
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,mongodb" />
  </a>
</p>

## Introduction

This library management system interacts with a MongoDB database to perform the following tasks:

- Insert a book into the database.
- Display a list of all books in your library.
- Find a book by its name.
- Display only read books.
- Display only books to read.
- Mark a book as read.
- Find books by a specific author.
- Display a list of authors in your library.
- Delete a book from your library.
- Remove a book from your wishlist.
- Add a book to your favorites.
- View your favorite books.

## Installation

Before running the program, ensure you have the necessary Python packages installed. You can install them using pip:

```bash
pip install pymongo
```

## Usage

1. Make sure you have MongoDB installed and running on your system.

2. Configure the MongoDB connection settings in the `BooksAPI.client` module by setting the `MONGO_URL` variable.

3. Save the provided code in a Python file, for example, `library.py`.

4. Run the application by executing the Python file:

   ```bash
   python library.py
   ```

5. Follow the on-screen instructions to interact with the library management system.

## Available Commands

Here are the available commands within the CLI:

- `show all`: Show all books in your library.
- `find`: Find a book by its name.
- `only readed`: Show only read books.
- `to read`: Show only books to read.
- `readed`: Mark a book as read.
- `by author`: Find books by a specific author.
- `authors`: Show a list of authors in your library.
- `delete book`: Delete a book from your library.
- `out wishlist`: Remove a book from your wishlist.
- `wishlist`: Show books in your wishlist.
- `favorite`: Add a book to your favorites.
- `view favorites`: View your favorite books.
- `add`: Add a new book to your library.
- `exit`: Exit the program.

Certainly, here's a section for usage examples specific to your library management system:

## Usage Examples

- Show all books in your library:

  ```bash
  python library.py show all
  ```

- Find a book by its name:

  ```bash
  python library.py find "Book Name"
  ```

- Display only read books:

  ```bash
  python library.py only readed
  ```

- Display only books to read:

  ```bash
  python library.py to read
  ```

- Mark a book as read:

  ```bash
  python library.py readed "Book Name"
  ```

- Find books by a specific author:

  ```bash
  python library.py by author "Author Name"
  ```

- Show a list of authors in your library:

  ```bash
  python library.py authors
  ```

- Delete a book from your library:

  ```bash
  python library.py delete book "Book Name"
  ```

- Remove a book from your wishlist:

  ```bash
  python library.py out wishlist "Book Name"
  ```

- Add a book to your favorites:

  ```bash
  python library.py favorite "Book Name"
  ```

- View your favorite books:

  ```bash
  python library.py view favorites
  ```

- Add a new book to your library:

  ```bash
  python library.py add
  ```

- Exit the program:

  ```bash
  python library.py exit
  ```

These are some usage examples to help you interact with the library management system via the command-line interface. You can run these commands in your terminal to perform various operations on your library.

## Contributing

This project is not entirely public as it's a personal project. However, if you're interested in contributing in any way or have suggestions, I'm open to receiving contributions. If you have questions or comments, you can contact me.

## Author

- [Pablo Solbal](https://github.com/pablossolbal)

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](LICENSE) file for details.
