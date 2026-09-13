# Redynox Python Developer Internship

This repository contains the solutions for the Redynox Python Developer Internship Task Assignment.

## Project Structure

```text
redynox-python-internship/
├── task1-backend/
├── task2-automation/
├── screenshots/
├── .gitignore
└── README.md
```

## Task 1: Task Management System

Backend REST API built using Python, FastAPI, SQLAlchemy, and SQLite.

### Setup

```text
cd task1-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```
uvicorn app.main:app --reload --port 8001
```

Swagger documentation:

[http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)