# Backend Authentication & Task Management API

A secure and scalable backend REST API built using **Django** and **Django REST Framework**, implementing **JWT-based authentication** and **CRUD operations on tasks**.  
This project was developed as part of a **Backend Developer Internship Assignment** and includes complete **Swagger API documentation** along with a **frontend demo video**.

---

## 📌 Project Overview

This backend application provides:

- Secure user registration and login
- JWT-based authentication for protected routes
- Full CRUD operations on tasks
- Clean and scalable API structure
- Interactive Swagger & ReDoc API documentation
- MySQL database integration
- Frontend demo to validate real API usage

The project follows backend best practices for **security**, **maintainability**, and **scalability**.

---

## 🚀 Features

### 🔐 Authentication
- User registration with password hashing
- User login with JWT token generation
- Token-protected API endpoints

### 📝 Task Management (CRUD)
- Create a task
- Retrieve all tasks
- Update a task
- Delete a task

### 📄 API Documentation
- Swagger UI for interactive API testing
- ReDoc UI for structured documentation

### 🛡️ Security & Best Practices
- JWT-based stateless authentication
- Input validation using DRF serializers
- Environment variables managed via `.env`
- Scalable and modular Django project structure

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Django, Django REST Framework |
| Authentication | JWT (JSON Web Tokens) |
| Database | MySQL |
| API Docs | Swagger (drf-yasg), ReDoc |
| Language | Python |
| Frontend | Separate frontend (demo video provided) |

---

## 📂 API Endpoints

### Authentication
| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | Login and receive JWT token |

### Task Management
| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/create-task/` | Create a new task |
| GET | `/get-tasks/` | Get all tasks |
| PUT | `/update-task/{id}/` | Update a task |
| DELETE | `/delete-task/{id}/` | Delete a task |

> 🔒 All task-related endpoints require JWT authentication.

---

## 📘 API Documentation

After starting the development server, access:

- **Swagger UI**  
  http://127.0.0.1:8000/swagger/

- **ReDoc UI**  
  http://127.0.0.1:8000/redoc/

Swagger provides an interactive interface to test all API endpoints.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/afrozeverse/backend_auth_crud_api.git
cd backend_auth_crud_api
### 2️⃣ Create a Virtual Environment
python -m venv venv
Activate it:

Windows

venv\Scripts\activate
Linux / macOS

source venv/bin/activate
### 3️⃣ Install Dependencies
pip install -r requirements.txt
### 4️⃣ Environment Variables
Create a .env file in the project root:

SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
The .env file is already added to .gitignore.

### 5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
### 6️⃣ Run the Server
python manage.py runserver
🎥 Frontend Demo
A frontend interface was created to demonstrate authentication and task CRUD operations using this backend API.

📺 Demo Video:
https://youtu.be/dqS34amKjKo

📈 Scalability Notes
This backend is designed with scalability in mind:

Stateless JWT authentication
Modular Django app structure
Easily extendable to:
Role-based access control (Admin/User)
Redis caching
Dockerized deployment
Load balancing (Nginx)
Microservices architecture

✅ Assignment Requirements Coverage

✅ Secure authentication (JWT)

✅ CRUD APIs

✅ Database integration

✅ API documentation (Swagger)

✅ Frontend demonstration

✅ Clean and scalable structure

✅ Security best practices

## Frontend Note

A basic frontend UI was developed to demonstrate authentication and task CRUD functionality.
Due to the backend-focused nature of this assignment, the frontend code is not included in this repository.

A complete working demo is provided via video:
https://youtu.be/dqS34amKjKo

Frontend source code can be shared upon request.

👨‍💻 Author

Afroze Ali

Backend Developer Intern Applicant

GitHub: https://github.com/afrozeverse
