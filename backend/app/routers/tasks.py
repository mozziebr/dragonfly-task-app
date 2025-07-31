"""
API router for task-related endpoints.
"""
from typing import Generator

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.database import SessionLocal
from app.models import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db() -> Generator[Session, None, None]:
    """
    Database session dependency - handles session lifecycle
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)) -> Task:
    """
    Create a new task
    """
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)) -> list[Task]:
    """
    Get all tasks
    """
    return db.query(Task).all()


@router.patch("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)
) -> Task:
    """
    Update a task by ID
    """
    db_task = db.query(Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update fields from request
    for k, v in task.dict().items():
        setattr(db_task, k, v)

    db.commit()
    db.refresh(db_task)

    # Need explicit typing here for mypy - TODO: check if still needed
    result: Task = db_task
    return result


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    """
    Delete a task by ID
    """
    task = db.query(Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
    return {"ok": True}
