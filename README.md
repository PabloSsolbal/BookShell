# Bookshell

Welcome to my personal project repository, Bookshell. This project consists of a small front-end project as a reading interface, a very simple API to communicate with the front-end and manage the cloud-hosted database, and finally a personal CLI that allows me to perform various CRUD operations on my database. It's a small project where I had the opportunity to use different technologies and connect everything to make it functional.

## Technologies

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=html,css,js,py,fastapi,mongodb" />
  </a>
</p>

## content

- [Features](./README#features)
- [Getting Started](./README#getting-started)
- [Usage](./README#usage)
- [Contributing](./README#contributing)
- [Author](./README#author)
- [License](./README#license)

## About

The idea for this project came about because I enjoy reading a lot and needed a way to organize my books. While there are many applications where I could have done that, I decided to develop something personally. That's when I set up the CLI and used a local Mongo database. After that, some people asked me for my book list, so to practice some things and put together a good project, I decided to set up an API and create a web interface to display my list of books. This way, I only need to share a link to the people view the updated list.

## DEMO

You can check the [video demo](https://youtu.be/qE1CehGVlSs) of the project.

## Features

**API**  

- Built with FastAPI.
- Mongo database.
- Provides different CRUD operations.
- Module to manage the DB.
- Models and schemas.

**CLI**

- Builded using OOP in pure Python.
- Uses the same db manager as the API.
- Provides all methods for the CRUD operations.
- Easy to use.

**web Interface**

- Buil with core wev techs.
- Shows data updated dinamically.
- Minimalist design.

## Getting Started

**How i can use for my library?**  
If you want to use this minimalistic system to manage follow the next steps:

First of all I recommend you to use a virtual enviroment.
So you can clone this repository:

```bash
git clone https://github.com/PabloSsolbal/BookShell.git
```

If you don't know how to set a virtual enviroment go to [Set Venv](./README#set-venv)  

Then run the following command to install the necesary dependencies:  

```bash
pip install -r requirements.txt
```

Or install by your own

- Python 3.9 or higher.
- FastAPI
- Uvicorn
- Pymongo
- Pydantic

You need to have your own Mongo database to use the system, if you don't know how to get a Mongo DB check these videos, can be a local or atlas Db:

Then you have a Mongo DB, create a `client.py` in the **`BooksAPI`** folder.  
The `client.py` needs some things to work:

```py
import os

MONGO_URL="" #This is the URI to connect to your database

urls=["*"] # The list of allowed origins to call your API, you can set as "*" to allow all

def get_allowed_origins():
  global urls
  """
    Here can be a code to return the allowed origins based on different conditions, but sure you can return the urls list to avoid any problem
  """
  return urls

  description="" #Description of the API, can be an Empty string
```

And thats all, you has configured the client to the db_manager. Probably you dont want to use the `main.py` to run the API so you cant set the things as default.

## Usage

## Set Venv

## Contributing

This project is not entirely public as it's a personal project. However, if you're interested in contributing in any way or have suggestions, I'm open to receiving contributions. If you have questions or comments, you can contact me.

If you come across an error or identify an issue, please create an "Issue" in this repository. Provide as much detail as possible about the problem.

## Author

- [Pablo Solbal](https://github.com/pablossolbal)

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](LICENSE) file for details.
