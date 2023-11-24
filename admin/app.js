import { API } from "./config.js";

const ViewBooksArea = document.getElementById("ViewBooksArea");
const Books = document.querySelector(".Books");
const BookNameInput = document.getElementById("Name");
const BookAuthorInput = document.getElementById("Author");
const WishListOptions = document.querySelector(".WishListOptions");
const MessageContainer = document.querySelector(".MessageContainer");
const Filter = document.getElementById("Filter");
const ThemeButton = document.querySelector(".NavBar button");

let readed = true;
let wishlist = false;

let BooksData = [];
let LastAPICall = API.GetAll;
let LastTitle = "All Books";

let Title = document.createElement("div");
Title.classList.add("Title");

let ReadBookBtn = `<button class="ReadBook">Read</button>`;
let UnreadBookBtn = `<button class="UnreadBook">Unread</button>`;
let FavoriteBookBtn = `<button class="FavoriteBook">Favorite</button>`;
let UnFavoriteBookBtn = `<button class="UnFavoriteBook">Unfavorite</button>`;
let OutOfWishListBtn = `<button class="OutWishList">Wishlist Out</button>`;
let IntoWishListBtn = `<button class="InWishList">Wishlist In</button>`;

Filter.addEventListener("change", () => {
  let Books = document.querySelectorAll(".Book");
  Books.forEach((Book) => {
    if (!Book.querySelector(".Name").textContent.includes(Filter.value)) {
      Book.classList.add("hidden");
    } else {
      Book.classList.remove("hidden");
    }
  });

  if (Filter.value === "") {
    Books.forEach((Book) => Book.classList.remove("hidden"));
  }
});

const ShowMessage = (message) => {
  MessageContainer.querySelector(".Message").textContent = message;
  MessageContainer.classList.add("Show");
  setTimeout(() => {
    MessageContainer.classList.remove("Show");
  }, 1200);
};

const ErrorMessage = (message) => {
  const ErrorDiv = document.createElement("div");
  ErrorDiv.classList.add("Error");
  ErrorDiv.classList.add("Book");
  ErrorDiv.innerHTML = `<div class="ErrorMessage">${message}</div>`;

  Books.innerHTML = "";
  Books.appendChild(ErrorDiv);
  Title.textContent = message;
  ViewBooksArea.prepend(Title);
};

const InputValidation = (input) => {
  let ValidationRegex = /^[a-zA-Z0-9  _\- \.]*$/;
  return ValidationRegex.test(input) && input !== "";
};

const AppendButtons = (Keys, Book) => {
  let Actions = [];
  if (
    Keys.includes("isReaded") &&
    Keys.includes("wishList") &&
    Keys.includes("favorite")
  ) {
    if (Book.isReaded == true && Book.favorite == true) {
      Actions.push(UnFavoriteBookBtn);
    }
    if (Book.isReaded == true) {
      Actions.push(UnreadBookBtn);
    }
    if (Book.isReaded === false && Book.wishList === false) {
      Actions.push(ReadBookBtn);
      Actions.push(IntoWishListBtn);
    } else if (
      Book.isReaded === true &&
      Book.wishList === false &&
      Book.favorite === false
    ) {
      Actions.push(FavoriteBookBtn);
    } else if (Book.isReaded === false && Book.wishList === true) {
      Actions.push(OutOfWishListBtn);
    }
  }
  return Actions;
};

const CreateBooks = () => {
  Books.classList.remove("Authors");
  Books.innerHTML = "";
  const BooksFragment = document.createDocumentFragment();
  for (let Book of BooksData) {
    const BookDiv = document.createElement("div");
    BookDiv.classList.add("Book");
    BookDiv.innerHTML = `
        <div class="Name">${Book.name}</div>
        <div class="Author">${Book.author}</div>
        <div class="Actions">
        <button class="DeleteBook">Delete</button>
        </div>
        `;
    let Keys = Object.entries(Book).map((key) => key[0]);
    let Actions = BookDiv.querySelector(".Actions");
    Actions.innerHTML += AppendButtons(Keys, Book).join("");

    if (Book.isReaded === false) {
      BookDiv.classList.add("NotReaded");
    }

    BooksFragment.appendChild(BookDiv);
  }
  Books.appendChild(BooksFragment);
  ViewBooksArea.prepend(Title);
};

const CreateAuthors = async () => {
  let Response = await fetch(API.GetAuthors);
  let Authors = await Response.json();

  Books.innerHTML = "";
  const AuthorsFragment = document.createDocumentFragment();

  for (let Author of Authors) {
    let AuthorDiv = document.createElement("div");
    AuthorDiv.classList.add("Book");

    AuthorDiv.innerHTML = `
        <div class="AuthorName Name">${Author}</div>
        <div class="AuthorActions">
        <button class="GetByAuthor">Books</button>
        </div>
        `;
    AuthorsFragment.appendChild(AuthorDiv);
  }
  Books.classList.add("Authors");
  Books.appendChild(AuthorsFragment);
  ViewBooksArea.prepend(Title);
};

const GetBooks = async (EndPoint = API.GetAll, TitleName = "All Books") => {
  LastAPICall = EndPoint;
  LastTitle = TitleName;
  try {
    let Response = await fetch(EndPoint);
    const Data = await Response.json();
    if (Data.hasOwnProperty("detail")) {
      ErrorMessage(Data.detail);
      return;
    }
    BooksData = Data;
    Title.textContent = TitleName;
    CreateBooks();
  } catch (e) {
    ErrorMessage("An Error Ocurred");
    return;
  }
};

const AddABook = async (readed, wishlist) => {
  if (
    !InputValidation(BookNameInput.value) ||
    !InputValidation(BookAuthorInput.value)
  ) {
    return;
  }
  let data = {
    name: BookNameInput.value,
    author: BookAuthorInput.value,
    readed,
    wishList: wishlist,
    favorite: false,
  };

  let options = {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  try {
    let Response = await fetch(API.PostBook, options);
    let Message = await Response.json();
    ShowMessage(Message.message);
    GetBooks(LastAPICall, Title.textContent);
  } catch (e) {
    ErrorMessage("An Error Ocurred");
    return;
  }
  BookNameInput.value = "";
  BookAuthorInput.value = "";
  wishlist = false;
  readed = true;
};

const DeleteBook = async (name) => {
  let options = {
    method: "DELETE",
  };
  let Response = await fetch(API.DeleteOne(name), options);
  let Message = await Response.json();
  ShowMessage(Message.message);
  GetBooks(LastAPICall, Title.textContent);
};

const BookStatus = async (EndPoint, Title, Redirection = API.GetAll) => {
  let options = {
    method: "PUT",
  };
  let Response = await fetch(EndPoint, options);
  let Message = await Response.json();
  ShowMessage(Message.message);
  GetBooks(Redirection, Title);
};

document.querySelectorAll("input").forEach((input) => {
  input.addEventListener("change", () => (input.style.color = "#000"));
});

document.addEventListener("DOMContentLoaded", () => {
  GetBooks();
});

document.addEventListener("click", (e) => {
  if (e.target.matches(".Readed") || e.target.matches(".UnReaded")) {
    document.querySelectorAll(".ReadedOptions button").forEach((btn) => {
      btn.classList.remove("SelectedR");
    });
    e.target.classList.add("SelectedR");
  }
  if (e.target.matches(".WishListTrue") || e.target.matches(".WishListFalse")) {
    document.querySelectorAll(".WishListOptions button").forEach((btn) => {
      btn.classList.remove("SelectedW");
    });
    e.target.classList.add("SelectedW");
  }
  if (e.target.matches(".Readed")) {
    readed = true;
    WishListOptions.classList.add("hidden");
    WishListOptions.previousElementSibling.classList.add("hidden");
  }
  if (e.target.matches(".UnReaded")) {
    readed = false;
    WishListOptions.classList.remove("hidden");
    WishListOptions.previousElementSibling.classList.remove("hidden");
  }
  if (e.target.matches(".WishListTrue")) {
    wishlist = true;
  }
  if (e.target.matches(".WishListFalse")) {
    wishlist = false;
  }
  if (e.target.matches(".AddBook")) {
    AddABook(readed, wishlist);
    WishListOptions.classList.add("hidden");
    WishListOptions.previousElementSibling.classList.add("hidden");
  }
  if (e.target.matches(".DeleteBook")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    DeleteBook(name);
  }

  if (e.target.matches(".ButtonArea button")) {
    if (
      e.target.textContent == "Authors" ||
      e.target.textContent == "Search" ||
      e.target.textContent == "Close"
    ) {
      if (e.target.textContent == "Authors") {
        Title.textContent = "Authors";
        eval(`${e.target.classList[0]}()`);
      }
      if (e.target.textContent == "Search" || e.target.textContent == "Close") {
        document.querySelector(".SearchForm").classList.toggle("Display");
        document.querySelector(".Form").classList.toggle("Display");
        e.target.textContent == "Search"
          ? (e.target.textContent = "Close")
          : (e.target.textContent = "Search");
      }
      return;
    }
    let action = e.target.classList[0];
    GetBooks(API[action], e.target.textContent);
  }

  if (e.target.matches(".GetByAuthor")) {
    GetBooks(
      API.GetByAuthor(
        e.target.parentElement.previousElementSibling.textContent
      ),
      `Books Of ${e.target.parentElement.previousElementSibling.textContent}`
    );
  }

  if (e.target.matches(".AuthorSearch") || e.target.matches(".NameSearch")) {
    document.querySelectorAll(".TypeOfSearch button").forEach((btn) => {
      btn.classList.remove("SelectedS");
    });
    e.target.classList.add("SelectedS");
  }
  if (e.target.matches(".SearchBy")) {
    let Value = document.getElementById("SearchInput").value;
    document.getElementById("SearchInput").value = "";
    if (!InputValidation(Value)) {
      return;
    }
    document.querySelector(".SelectedS").classList.contains("NameSearch")
      ? GetBooks(API.GetByName(Value), Value)
      : GetBooks(API.GetByAuthor(Value), Value);
  }

  if (e.target.matches(".Author")) {
    GetBooks(
      API.GetByAuthor(e.target.textContent),
      `Books of ${e.target.textContent}`
    );
  }

  if (e.target.matches(".FavoriteBook")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    BookStatus(API.PutInFavorites(name), LastTitle, LastAPICall);
  }
  if (e.target.matches(".OutWishList")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    BookStatus(API.PutOutWishList(name), LastTitle, LastAPICall);
  }
  if (e.target.matches(".ReadBook")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    BookStatus(API.PutReaded(name), LastTitle, LastAPICall);
  }
  if (e.target.matches(".UnreadBook")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    BookStatus(API.UnreadOne(name), LastTitle, LastAPICall);
  }
  if (e.target.matches(".UnFavoriteBook")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    BookStatus(API.UnfavoriteOne(name), LastTitle, LastAPICall);
  }
  if (e.target.matches(".InWishList")) {
    let name =
      e.target.parentElement.parentElement.querySelector(".Name").textContent;
    BookStatus(API.IntoWishList(name), LastTitle, LastAPICall);
  }
});

document.addEventListener("keyup", (e) => {
  if (e.key == "Enter") {
    if (document.querySelector(".SearchForm").classList.contains("Display")) {
      document.querySelector(".SearchBy").click();
    } else if (document.querySelector(".Form").classList.contains("Display")) {
      document.querySelector(".AddBook").click();
    }
  }
});

ThemeButton.addEventListener("click", () => {
  document.body.classList.toggle("DarkTheme");
  ThemeButton.querySelector("i").classList.contains("fa-moon")
    ? ThemeButton.querySelector("i").classList.replace("fa-moon", "fa-sun")
    : ThemeButton.querySelector("i").classList.replace("fa-sun", "fa-moon");
});
