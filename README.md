## 📦 Mini Trello API
Mini Trello API is a lightweight Trello-inspired task management API built with Django and Django REST Framework. This project allows authenticated users to create boards, lists, and tasks—providing a solid foundation for integrating with frontend applications like React, Vue, or mobile apps.

🚀 Features
🔐 Token-based Authentication (JWT ready)

🗂️ Boards: Create, update, delete boards

📋 Lists: Organize tasks within boards

✅ Tasks: Add, update, and move tasks between lists

🧑‍💻 User Registration and Login

🔄 RESTful endpoints with JSON responses

🛠️ Tech Stack
- Python 3
- Django
- Django REST Framework
- SQLite (default, easy to switch)



📦 Installation
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
- *POST /users/register/* – Register a new user
- *POST /users/login/* – Login and get token
- *GET /users/profile/* – Allows an authenticated user to view his details
- *PUT /users/profile/* – Allows an authenticated user to edit his details


### 🔁 API Endpoints Overview
Boards:
- GET */boards/* – List all boards
- POST */boards/* – Create a board
- GET */boards/<slug>/* – Retrieve a board
- PUT */boards/<slug>/* – Update a board
- DELETE */boards/<slug>/* – Delete a board


Tasks:

- GET /tasks/ – List all tasks

- POST /tasks/ – Create a task

- GET /tasks/<id>/ – Retrieve a task

- PUT /tasks/<id>/ – Update a task

- DELETE /tasks/<id>/ – Delete a task



Use Swagger at `http://127.0.0.1:8000` or Postman or any REST client to interact with the API endpoints.


