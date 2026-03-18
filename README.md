    # Group 11 — Advanced Programming (DIT 3-2 2526)

This repository contains the Group 11 project for the **Advanced Programming** course. Our goal was to learn and apply a proper development workflow using **Flask**, **Git/GitHub**, and **MySQL** while building a working authentication system.

---

## ✅ What We Built

A **Flask web application** with a **basic login & registration system** backed by a **MySQL** database. Key learning outcomes include:

- Setting up a local **Python development environment (venv)**
- Building a Flask app with proper **project structure** (templates, static files, models, migrations)
- Using **Git** for version control and collaboration
- Writing clear **GitHub documentation** (this README + docs)
- Implementing **user authentication** (register/login/logout)
- Persisting users in a **MySQL database** via **SQLAlchemy**

---

## 🧪 What You’ll Find in This Repo

- `app.py` — Flask application entry point
- `models/` — database model definitions (e.g., users)
- `migrations/` — Alembic migrations for schema management
- `templates/` — HTML templates for login/register pages
- `static/` — CSS/JS assets for front-end styling and form behavior
- `requirements.txt` — Python dependencies

---

## 🚀 How to Run Locally

### 1) Setup Python virtual environment

```bash
python -m venv env
```

### 2) Activate the environment

**Windows PowerShell**
```powershell
.
\env\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure your database

Create a MySQL database and update `config.py` (or environment variables) with your connection details.

### 5) Initialize the database (migrations)

```bash
python create_db.py
```

### 6) Run the app

```bash
python app.py
```

Open your browser at: `http://127.0.0.1:5000`

---

## 🧑‍🤝‍🧑 Team Members

- Carl Denzel G. Huerto
- Franz Angelo R. Loma
- Rio Angela T. Nava
- Kenneth P. Osorio
- Kristala P. Patron

---

## 📚 Documentation

- [Project documentation](https://docs.google.com/document/d/1SohkNUJou3Z_-nrkS2Z8xF-PTEZ4Qc4SItAMMkjK-88/edit?usp=sharing)

---

## 💡 Notes

This project is built as part of the Advanced Programming subject, focusing on real-world practices such as:

- Proper workspace setup
- Git-based collaboration (feature branches, commits, pull requests)
- Building a working Flask app with a database backend
- Understanding the basic workflow of a real software project

