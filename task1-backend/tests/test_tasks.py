from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database.database import Base, get_db
from app.main import app
from app.models.task import Task  # noqa: F401

# In-memory SQLite is shared across connections with StaticPool.
SQLALCHEMY_DATABASE_URL = "sqlite://"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Finish internship task", "description": "Build a REST API"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Finish internship task"
    assert data["description"] == "Build a REST API"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_task_by_id():
    created = client.post("/tasks", json={"title": "Read a task"}).json()
    response = client.get(f"/tasks/{created['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Read a task"


def test_get_task_not_found():
    response = client.get("/tasks/99999")
    assert response.status_code == 404


def test_update_task():
    created = client.post("/tasks", json={"title": "Old title"}).json()
    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": "Updated title",
            "description": "Updated description",
            "completed": True,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated title"
    assert data["description"] == "Updated description"
    assert data["completed"] is True


def test_update_task_not_found():
    response = client.put(
        "/tasks/99999",
        json={"title": "Does not exist"},
    )
    assert response.status_code == 404


def test_delete_task():
    created = client.post("/tasks", json={"title": "Delete me"}).json()
    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == 204

    follow_up = client.get(f"/tasks/{created['id']}")
    assert follow_up.status_code == 404


def test_delete_task_not_found():
    response = client.delete("/tasks/99999")
    assert response.status_code == 404


def test_create_task_empty_title():
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 422
