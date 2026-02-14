# 📝 Flask To‑Do App

A simple and modern To‑Do web application built with **Flask**, **SQLAlchemy**, and **Bootstrap**.  
The app provides both a clean HTML interface and a fully functional **REST API**.

---

## 🚀 Features

- Create, toggle, and delete tasks  
- Modern UI using Bootstrap 5 and Bootstrap Icons  
- SQLite database (no setup required)  
- Full REST API:
  - `GET /api/todos`
  - `POST /api/todos`
  - `PATCH /api/todos/<id>`
  - `DELETE /api/todos/<id>`
- Clean and minimal project structure  
- Runs out of the box

---

## 📁 Project Structure

todo_app/ │ ├── app.py ├── models.py ├── requirements.txt │ └── templates/ └── index.html


---

pip install -r requirements.txt

python app.py

http://127.0.0.1:5000


🧱 Technologies Used
- Python 3.14.3
- Flask
- SQLAlchemy
- SQLite
- Bootstrap 5
- Bootstrap Icons

📌 Notes
- The todos.db database file is created automatically.
- This project is a great foundation for additional features such as:
- Pagination
- Filtering & sorting
- User authentication
- JavaScript frontend
- Deployment (Docker, Render, Railway)
