from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate
from fastapi import HTTPException

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())  # Unpack the Pydantic TaskCreate model
    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)  # Refresh to get the task with the assigned ID
        return db_task  # Return the created task
    except Exception as e:
        db.rollback()  # Rollback in case of an error
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        for field, value in task.dict().items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

def delete_all_tasks(db: Session):
    db.query(Task).delete()
    db.commit()