"""
SQLAlchemy ORM models for the backend.
"""
from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class Task(Base):
    """
    ORM model representing a task in the database.
    """

    __tablename__ = "tasks"
    id = Column(
        Integer, primary_key=True, index=True, doc="Unique identifier for the task."
    )
    title = Column(String, index=True, doc="Title or description of the task.")
    completed = Column(Boolean, default=False, doc="Completion status of the task.")
