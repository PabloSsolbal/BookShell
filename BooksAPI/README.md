# Books API Documentation

The Books API is designed to provide access to data from a personal Books database. It offers endpoints to retrieve information about books in the library, wishlist, and by a specific author. This documentation provides details on the available endpoints, their functionality, and usage.

## Technologies

**Technologies Used**
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=fastapi,mongodb" />
  </a>
</p>

## Authentication

The Books API does not require authentication and allows access from any origin. CORS (Cross-Origin Resource Sharing) is enabled to ensure compatibility with web applications.

## Endpoints

### 1. Get Wishlist

- **Endpoint:** `/wishlist`
- **Method:** GET
- **Description:** Returns a list of books in the wishlist.
- **Response:** JSON array containing book details.
  - `name` (string): The name of the book.
  - `author` (string): The author of the book.

#### Example Request

```http
GET /wishlist
```

#### Example Response

```json
[
  {
    "name": "Book 1",
    "author": "Author A"
  },
  {
    "name": "Book 2",
    "author": "Author B"
  }
]
```

### 2. Get Library

- **Endpoint:** `/library`
- **Method:** GET
- **Description:** Returns a list of books in the library, along with their read status.
- **Response:** JSON array containing book details.
  - `name` (string): The name of the book.
  - `author` (string): The author of the book.
  - `isReaded` (boolean): Indicates if the book has been read (`true`) or not (`false`).

#### Example Request

```http
GET /library
```

#### Example Response

```json
[
  {
    "name": "Book 3",
    "author": "Author A",
    "isReaded": true
  },
  {
    "name": "Book 4",
    "author": "Author B",
    "isReaded": false
  }
]
```

### 3. Get Books by Author

- **Endpoint:** `/books/{author}`
- **Method:** GET
- **Description:** Returns a list of books by the specified author.
- **Parameters:**
  - `author` (string): The name of the author.
- **Response:** JSON array containing book details.
  - `name` (string): The name of the book.
  - `author` (string): The author of the book.
  - `isReaded` (boolean): Indicates if the book has been read (`true`) or not (`false`).

#### Example Request

```http
GET /books/Author A
```

#### Example Response

```json
[
  {
    "name": "Book 1",
    "author": "Author A",
    "isReaded": true
  },
  {
    "name": "Book 3",
    "author": "Author A",
    "isReaded": false
  }
]
```

## Response Codes

- `200 OK`: The request was successful, and the response contains the expected data.
- `404 Not Found`: The requested resource or endpoint does not exist.
- `500 Internal Server Error`: An internal server error occurred.

## Error Handling

The API provides basic error handling. In case of errors, it will return an appropriate HTTP status code along with an error message.

## Rate Limiting

The API does not currently implement rate limiting.

## Author

- [Pablo Solbal](https://github.com/pablossolbal)

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](LICENSE) file for details.
