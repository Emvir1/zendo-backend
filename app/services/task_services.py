from app.extensions import db
from app.models.task_model import Task


def get_all_tasks():
    tasks = Task.query.all()
    return [task.all_tasks() for task in tasks], 200


def create_task(data):
    task = Task(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status", "pending"),
        user_id=data["user_id"],
    )
    db.session.add(task)
    db.session.commit()
    return task.get_task(), "Task created successfully", 201
