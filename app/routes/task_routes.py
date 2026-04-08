from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.resources.task_resources import TaskListResource, TaskDetailResource

task_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")
task_list = TaskListResource()
task_detail = TaskDetailResource()


@task_bp.get("/")
@jwt_required()
def get_tasks():
    return task_list.get()


@task_bp.post("/")
@jwt_required()
def create_task():
    return task_list.post()


@task_bp.get("/<int:task_id>")
@jwt_required()
def get_task(task_id):
    return task_detail.get(task_id)


@task_bp.patch("/<int:task_id>")
@jwt_required()
def update_task(task_id):
    return task_detail.patch(task_id)


@task_bp.delete("/<int:task_id>")
@jwt_required()
def delete_task(task_id):
    return task_detail.delete(task_id)
