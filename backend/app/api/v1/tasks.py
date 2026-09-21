from fastapi import APIRouter
from app.models.task import Task

router = APIRouter()

tasks_db = []

@router.post("/")
async def create_task(task: Task):
    tasks_db.append(task.dict())
    return {"message": "Task created", "task": task}

@router.get("/")
async def list_tasks():
    return tasks_db

