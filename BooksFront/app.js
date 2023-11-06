/**
 * ! Creates a list of books app from an API
 * ? This code manages a web application for tracking books in a wishlist and library.
 * * It dynamically fetches data from an API, displays it, and allows user to switch between
 * *  their wishlist and library.
 */

// ? window variables to call the API
import { library, wishlist } from "./config.js";

// ? elements of the dom that we will use
/**
 * * title of the page
 * * books container
 * * buttons to change the content
 */
const title = document.querySelector(".title");
const books = document.querySelector(".books");
const btns = document.querySelectorAll(".btn");

// ? array to save the current data
let data = [];

// ? Functions to get the data from the API
/**
 *  * The function are asynchronous and returns a Promise.
 *  * Make an asynchronous HTTP request
 *  * The response will be a JSON object. Convert it to a JavaScript object
 *  * Store the data in the `data` variable.
 *  * Clear the body of the page. - ClearBody function
 *  * Create a list of books from the data. - CreateBooks function
 */

// ? Function to get the wishlist of books
const getWishlist = async () => {
  await fetch(wishlist)
    .then((res) => res.json())
    .then((res) => {
      data = res;
    });
  clearBody();
  createBooks();
};

// ? Function to get the library of books

const getLibrary = async () => {
  await fetch(library)
    .then((res) => res.json())
    .then((res) => {
      data = res;
    });
  clearBody();
  createBooks();
};

// ? Function to create the list of books
/**
 * * This function creates a list of book items from the data.
 * * Create two empty arrays to store the read and unread books.
 * * Iterate through the data array.
 * * Create a new book item element.
 * * Create two new text elements for the book name and author.
 * * Set the text content of the book name and author elements.
 * * Append the book name and author elements to the book item element.
 *
 * * If the book is not read, add it to the notReadedBooks array.
 * * Else add it to the readedBooks array.
 * * Combine the read and unread books arrays into a single array.
 *
 * * Iterate through the allBooks array and append each book item to the books container.
 */
const createBooks = () => {
  const readedBooks = [];
  const notReadedBooks = [];

  data.forEach((book) => {
    const bookItem = document.createElement("div");
    bookItem.classList.add("book");

    const bookName = document.createElement("div");
    bookName.classList.add("name");

    const bookAuthor = document.createElement("div");
    bookAuthor.classList.add("author");

    bookName.textContent = book.name;
    bookAuthor.textContent = book.author;

    bookItem.appendChild(bookName);
    bookItem.appendChild(bookAuthor);

    if (book.isReaded === false) {
      bookItem.classList.add("not-readed");
      notReadedBooks.push(bookItem);
    } else {
      readedBooks.push(bookItem);
    }
  });

  const allBooks = readedBooks.concat(notReadedBooks);

  allBooks.forEach((bookItem) => {
    books.appendChild(bookItem);
  });
};

// ? This function is a starter function that determines which function to call based on the parameter.
/**
 * * Check the parameter
 * * Change the title of the page.
 * * Call the function that corresponds to the parameter.
 */

const starter = (func) => {
  if (func === "wishlist") {
    title.textContent = "Wishlist";
    getWishlist();
  } else if (func === "library") {
    title.textContent = "Library";
    getLibrary();
  }
};

// ? This function is a wrapper function that calls the starter function with the specified content.
/**
 * * Check the parameter
 * * Calls the starter with the func based on parameter
 */

const call = (content) => {
  if (content === "Wishlist") {
    starter("wishlist");
  } else if (content === "Library") {
    starter("library");
  }
};

// ? Clear the html function -To blank the page before charge the books-
const clearBody = () => {
  books.innerHTML = "";
};

// ? This function iterates through the btns array and adds an event listener to each button.
/**
 * * Add an event listener to the button.
 * * Remove the "select" class from all buttons.
 * * Add the "select" class to the clicked button.
 * * Call the call function with the text content of the clicked button.
 */
btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    btns.forEach((btn) => {
      btn.classList.remove("select");
    });
    btn.classList.add("select");

    call(btn.textContent);
  });
});

// ? start the app with the wishlist content
starter("wishlist");
