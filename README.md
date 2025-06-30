## 📦 Mini Trello API
Mini Trello API is a lightweight Trello-inspired task management API built with Django and Django REST Framework. This project allows authenticated users to create and manage tasks across multiple boards.

### 🚀 Features
🔐 Token-based Authentication (JWT ready)

🗂️ Boards: Create, update, delete boards
- 👁️ Visibility: Make a board **private** or **public** 

✅ Tasks: Add, update, and move tasks between lists
- 📊 Status: **Todo, in-progress, Done** status can be set to tasks

🧑‍💻 User Registration and Login

🔄 RESTful endpoints with JSON responses


### 🛠️ Tech Stack
- Python 3
- Django
- Django REST Framework
- SQLite (default, easy to switch)



### 📦 Installation
Clone the Repository
`git clone https://github.com/johnpauljpc/mini_trello.git`
`cd mini_trello`

Create Virtual Environment & Activate
`python -m venv env`
`source env/bin/activate`  # On Windows use `env\Scripts\activate`

Install Dependencies
`pip install -r requirements.txt`

Run Migrations
`python manage.py migrate`

Start Development Server
`python manage.py runserver`

Access API at `http://127.0.0.1:8000/`

### 🔐 Authentication Endpoints
- **POST** /users/register/ – Register a new user
- **POST** /users/login/ – Login and get token
- **GET** /users/profile/ – Allows an authenticated user to view his details
- **PUT** /users/profile/ – Allows an authenticated user to edit his details


### 🔁 API Endpoints Overview
Boards:
- **GET** */boards/* – List all boards
- **POST** */boards/* – Create a board
- **GET** */boards/&lt;slug>/* – Retrieve a board
- **PUT** */boards/&lt;slug>/* – Update a board
- **DELETE** */boards&lt;slug>/* – Delete a board


Tasks:

- **GET** /tasks/ – List all tasks

- **POST** /tasks/ – Create a task

- **GET** /tasks/&lt;id>/ – Retrieve a task

- **PUT** /tasks/&lt;id>/ – Update a task

- **DELETE** /tasks/&lt;id>/ – Delete a task



Use Swagger at `http://127.0.0.1:8000` or Postman or any REST client to interact with the API endpoints.


