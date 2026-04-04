from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.resources.task_resources import TaskResource

task_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")
task_resource = TaskResource()


@task_bp.get("/")
@jwt_required()
def get_tasks():
    return task_resource.get_all()


@task_bp.post("/")
@jwt_required()
def create_task():
    return task_resource.post()


@task_bp.patch("/<int:task_id>")
@jwt_required()
def update_task(task_id):
    return task_resource.patch(task_id)


@task_bp.delete("/<int:task_id>")
@jwt_required()
def delete_task(task_id):
    return task_resource.delete(task_id)

@task_bp.get("/<int:task_id>")
@jwt_required()
def get_task(task_id):
    return task_resource.get_one(task_id)
