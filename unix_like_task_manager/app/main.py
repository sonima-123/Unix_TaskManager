from fastapi import FastAPI
from app.api import task_routes
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI(title="Unix-like Task Manager")
app.include_router(task_routes.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Hi, Welcome to the Unix Task Manager API"}