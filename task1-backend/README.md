# Task Management REST API

Redynox Python Developer Internship — Task 1.

A beginner-friendly REST API built with **Python**, **FastAPI**, **SQLAlchemy**, **SQLite**, and **Pydantic**. You can create, read, update, and delete tasks. The API is documented automatically and can be tested with Postman or pytest.

## Project structure

```
task1-backend/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── database/database.py    # SQLite engine, session, and get_db dependency
│   ├── models/task.py          # SQLAlchemy Task table
│   ├── schemas/task.py         # Pydantic request and response models
│   └── routes/tasks.py         # REST endpoints
├── tests/
│   └── test_tasks.py           # Automated API tests
├── pytest.ini                  # Lets pytest import the app package
├── requirements.txt
└── README.md
```

## Setup

From the `task1-backend` folder:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

The server starts at **http://127.0.0.1:8000**.

Interactive API docs (Swagger UI): **http://127.0.0.1:8000/docs**  
Alternative docs (ReDoc): **http://127.0.0.1:8000/redoc**

SQLite creates a `tasks.db` file in `task1-backend/` the first time you run the app. Records are not hardcoded; they are stored in this database.

## Endpoints

| Method | URL | Status codes | Description |
|--------|-----|--------------|-------------|
| POST | `/tasks` | 201, 422 | Create a task |
| GET | `/tasks` | 200 | List all tasks |
| GET | `/tasks/{id}` | 200, 404 | Get one task |
| PUT | `/tasks/{id}` | 200, 404, 422 | Replace a task |
| DELETE | `/tasks/{id}` | 204, 404 | Delete a task |

### Request body (POST and PUT)

```json
{
  "title": "Finish internship task",
  "description": "Build a REST API",
  "completed": false
}
```

- `title` is required and cannot be empty or only spaces.
- `description` is optional.
- `completed` is optional and defaults to `false`.

### Example response

```json
{
  "id": 1,
  "title": "Finish internship task",
  "description": "Build a REST API",
  "completed": false,
  "created_at": "2026-09-12T09:00:00"
}
```

## Test with Postman

1. Start the API with `uvicorn app.main:app --reload`.
2. Create a Postman collection named **Task Management API**.
3. Add these requests:

**Create task**
- Method: `POST`
- URL: `http://127.0.0.1:8000/tasks`
- Headers: `Content-Type: application/json`
- Body (raw JSON):

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

**List tasks**
- Method: `GET`
- URL: `http://127.0.0.1:8000/tasks`

**Get one task**
- Method: `GET`
- URL: `http://127.0.0.1:8000/tasks/1`

**Update task**
- Method: `PUT`
- URL: `http://127.0.0.1:8000/tasks/1`
- Body (raw JSON):

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread, coffee",
  "completed": true
}
```

**Delete task**
- Method: `DELETE`
- URL: `http://127.0.0.1:8000/tasks/1`

**Validation error**
- POST `/tasks` with `"title": ""` or `"title": "   "` and confirm the API returns **422**.

**Not found**
- GET, PUT, or DELETE `/tasks/99999` and confirm the API returns **404**.

You can also import the OpenAPI spec from `http://127.0.0.1:8000/openapi.json` into Postman.

## Run automated tests

```bash
pytest
```

Tests use an in-memory SQLite database so they do not change `tasks.db`.
