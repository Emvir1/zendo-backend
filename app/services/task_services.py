from http import HTTPStatus
from app.extensions import db
from app.models.task_model import Task
from app.models.list_model import List
from sqlalchemy import select


def get_all_tasks(user_id, list_id=None):

    query = select(Task).where(Task.user_id == int(user_id))

    if list_id:
        query = query.where(Task.list_id == int(list_id))

    tasks = db.session.scalars(query).all()

    return [task.get_task() for task in tasks], HTTPStatus.OK

def create_task(data):

    list_id = data.get("list_id")

    if list_id:
        list_obj = db.session.scalar(
            select(List).where(
                List.id == list_id,
                List.user_id == int(data["user_id"])
            )
        )

        if not list_obj:
            return {"message": "List not found"}, HTTPStatus.NOT_FOUND

    task = Task(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status", "pending"),
        user_id=int(data["user_id"]),
        list_id=list_id
    )

    db.session.add(task)
    db.session.commit()

    return task.get_task(), HTTPStatus.CREATED


def update_task(task_id, user_id, data):
    task = db.session.scalar(select(Task).where(Task.id == task_id, Task.user_id == int(user_id)))
    if not task:
        return None, HTTPStatus.NOT_FOUND

    if data.get("title") is not None:
        task.title = data["title"]
    if data.get("description") is not None:
        task.description = data["description"]
    if data.get("status") is not None:
        task.status = data["status"]
    if "list_id" in data:
        task.list_id = data["list_id"]

    db.session.commit()
    return task.get_task(), HTTPStatus.OK


def delete_task(task_id, user_id):
    task = Task.query.filter_by(id=task_id, user_id=int(user_id)).first()
    if not task:
        return None, HTTPStatus.NOT_FOUND

    db.session.delete(task)
    db.session.commit()
    return None, HTTPStatus.OK


def get_task_by_id(task_id, user_id):
    task = Task.query.filter_by(id=task_id, user_id=int(user_id)).first()
    if not task:
        return None, "Task not found", HTTPStatus.NOT_FOUND
    return task.get_task(), HTTPStatus.OK
