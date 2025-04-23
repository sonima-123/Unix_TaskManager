from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    name: str  
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class TaskOut(TaskBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime  

    class Config:
        from_attributes = True
