"""
Pydantic schemas for request and response validation.
"""
from pydantic import BaseModel


class TaskBase(BaseModel):
    """
    Base schema for a task, used as a parent for other schemas.
    """

    title: str
    completed: bool = False


class TaskCreate(TaskBase):
    """
    Schema for creating a new task.
    """

    pass


class TaskUpdate(TaskBase):
    """
    Schema for updating an existing task.
    """

    pass


class Task(TaskBase):
    """
    Schema for reading a task, including its ID.
    """

    id: int

    class Config:
        orm_mode = True
