"""
Main entry point for the FastAPI backend application.
"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import tasks

app = FastAPI(
    title="Task Management API", description="Backend API for managing tasks."
)

# Register routers
app.include_router(tasks.router)

# CORS middleware (allow all origins for development; restrict in production)
app.add_middleware(
    CORSMiddleware,
    # TODO: change to ["http://localhost:3000"] or your domain in production
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Only create tables if not in testing mode
if not os.getenv("TESTING"):
    Base.metadata.create_all(bind=engine)
