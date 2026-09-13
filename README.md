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

## Task 2: Automated CSV Report Generator

Python automation tool that processes employee CSV data and generates an automated report.

### Setup

```text
cd task2-automation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Run

python report_generator.py --input input/sample_data.csv

Generated report:
output/employee_report.txt

Execution log:
logs/automation.log

## Testing

Task 1 was tested for CRUD operations, validation, and error handling.

Task 2 was tested with valid CSV files, missing files, missing columns, invalid salary values, and empty CSV files.

## Screenshots

Testing and demonstration screenshots are available in the screenshots folder.

## Technologies

Python, FastAPI, SQLAlchemy, SQLite, Pandas, Pytest, Git, GitHub
