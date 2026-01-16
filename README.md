# Django Book Todo App

A simple beginner-friendly Django project with authentication and CRUD operations.

This app allows users to:

- Register
- Login / Logout
- Add books to a todo list
- Mark books as completed
- Delete books
- Each user has their own data

Built for learning Django basics.

## 🛠 Tech Stack

- Python 3
- Django
- SQLite (default Django database)

## 📁 Project Structure

```
booktodo/
├── manage.py
├── booktodo/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── books/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── migrations/
└── templates/
```

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

````bash
git clone https://github.com/Siratul804/django-book-todo
cd django-book-todo

### 2️⃣ Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows

### 3️⃣ Install dependencies
```bash
pip install django
````

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run development server

```bash
python manage.py runserver
```

Open browser:

```bash
http://127.0.0.1:8000/
```

## 🔐 Authentication URLs

| URL                 | Description       |
| ------------------- | ----------------- |
| `/register/`        | Register new user |
| `/accounts/login/`  | Login             |
| `/accounts/logout/` | Logout            |
| `/admin/`           | Django admin      |

## 📌 Notes

- SQLite database is used by default

- Database file is excluded from GitHub

- Uses Django built-in authentication

- Logout uses POST (secure)

## 📚 Learning Goals

This project helps understand:

- Django project structure

- Apps and models

- Authentication

- CRUD operations

- Templates

- Migrations

- Git & GitHub basics

## 🧑‍💻 Author

Siratul Islam
