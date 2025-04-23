from app.db.session import Base
from app.models.task_model import Task

# All models that inherit Base are imported here
__all__ = ["Base", "Task"]