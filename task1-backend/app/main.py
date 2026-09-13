from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.task import Task  # noqa: F401 - needed so create_all sees the table
from app.routes.tasks import router as tasks_router

# Create database tables if they do not already exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="A REST API for creating, reading, updating, and deleting tasks.",
    version="1.0.0",
)

app.include_router(tasks_router)
