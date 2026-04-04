from app.extensions import db
from app.models.task_model import Task


def get_all_tasks(user_id):
    tasks = Task.query.filter_by(user_id=int(user_id)).all()
    return [task.all_tasks() for task in tasks], 200


def create_task(data):
    task = Task(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status", "pending"),
        user_id=int(data["user_id"]),
    )
    db.session.add(task)
    db.session.commit()
    return task.get_task(), "Task created successfully", 201


def update_task(task_id, user_id, data):
    task = Task.query.filter_by(id=task_id, user_id=int(user_id)).first()
    if not task:
        return None, "Task not found", 404

    if data.get("title") is not None:
        task.title = data["title"]
    if data.get("description") is not None:
        task.description = data["description"]
    if data.get("status") is not None:
        task.status = data["status"]

    db.session.commit()
    return task.get_task(), "Task updated successfully", 200


def delete_task(task_id, user_id):
    task = Task.query.filter_by(id=task_id, user_id=int(user_id)).first()
    if not task:
        return None, "Task not found", 404

    db.session.delete(task)
    db.session.commit()
    return None, "Task deleted successfully", 200

def get_task_by_id(task_id, user_id):
    task = Task.query.filter_by(id=task_id, user_id=int(user_id)).first()
    if not task:
        return None, "Task not found", 404
    return task.get_task(), "Task retrieved successfully", 200
