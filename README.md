# 📝 Flask To‑Do App

Eine einfache, moderne To‑Do‑Webanwendung auf Basis von **Flask**, **SQLAlchemy** und **Bootstrap**.  
Die App bietet sowohl eine klassische HTML‑Oberfläche als auch eine vollständige **REST‑API**.

---

## 🚀 Features

- Aufgaben erstellen, abhaken und löschen  
- Moderne UI mit Bootstrap 5 und Bootstrap Icons  
- SQLite‑Datenbank (lokal, ohne Setup)  
- Vollständige REST‑API:
  - `GET /api/todos`
  - `POST /api/todos`
  - `PATCH /api/todos/<id>`
  - `DELETE /api/todos/<id>`
- Saubere Projektstruktur  
- Läuft ohne zusätzliche Konfiguration

---

## 📁 Projektstruktur
todo_app/ 
│ 
├── app.py 
├── models.py 
├── requirements.txt 
│ └── templates/ 
    └── index.html

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
