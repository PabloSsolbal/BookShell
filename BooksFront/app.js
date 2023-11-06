/**
 * @file
 * ? This JavaScript file is responsible for managing book data in a web application.
 * * It fetches book data from specified URLs, displays them in the document, and allows users to switch
 * * between different book categories, such as "Wishlist" and "Library," by clicking buttons.
 *
 * * Features:
 * * - Fetch book data from remote URLs and display it in the document.
 * * - Allow users to switch between "Wishlist" and "Library" views using buttons.
 * * - Dynamically create book elements based on the fetched data.
 * @author Pablo Solbal <pablossolbal@gmail.com>
 * @copyright Pablo Solbal 2023
 * @license Apache License Version 2.0
 */

// ? Import the urls object from the config.js file.
import { urls } from "./config.js";

// * URLs
let wishlist = urls.wishlist;
let library = urls.library;

// * DOM elements
const title = document.querySelector(".title");
const books = document.querySelector(".books");
const btns = document.querySelectorAll(".btn");

/**
 * * Fetch book data from a given URL, clear the current page content, and create book elements with the fetched data.
 * @param {string} url - The URL from which to fetch book data.
 */
const getBooksData = async (url) => {
  const response = await fetch(url);
  const data = await response.json();
  clearBody();
  createBooks(await data);
};

/**
 * * Create book elements based on the provided data and append them to the "books" container in the document.
 * @param {Array} data - An array of book data objects, each containing at least "name," "author," and "isReaded" properties.
 */
const createBooks = (data) => {
  // ? Separate books into readed and not readed categories
  const readedBooks = [];
  const notReadedBooks = [];
  const booksFragment = document.createDocumentFragment();

  // ? Iterate through the provided data to create book elements
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

  // ? Combine readed and not readed books, then append them to the document fragment, then append to the books container
  const allBooks = [...readedBooks, ...notReadedBooks];

  allBooks.forEach((bookItem) => {
    booksFragment.appendChild(bookItem);
  });

  books.appendChild(booksFragment);
};

/**
 * ? Change the text content of an HTML element with the id "title."
 * @param {string} text - The text to set as the new content of the element.
 */
const changeTitle = (text) => {
  title.textContent = text;
};

/**
 * * Change the title text and load books data based on the content provided.
 * @param {string} content - The content to set as the new title and determine which books data to load (e.g., "Wishlist" or "Library").
 */
const call = (content) => {
  changeTitle(content);

  if (content === "Wishlist") {
    getBooksData(wishlist);
  } else if (content === "Library") {
    getBooksData(library);
  }
};

/**
 *  ? Clear the html -To blank the page before charge the books-
 */
const clearBody = () => {
  books.innerHTML = "";
};

/**
 * ? Add a click event listener to the document that responds to button clicks with the class "btn."
 * * When a button is clicked, it updates the selected button's appearance, and calls the "call" function
 * with the text content of the clicked button.
 * @param {Event} e - The click event object.
 */
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("btn")) {
    btns.forEach((btn) => {
      btn.classList.remove("select");
    });
    e.target.classList.add("select");

    call(e.target.textContent);
  }
});

/**
 * ? Start the app with the wishlist content
 */
call("Wishlist");
