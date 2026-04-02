from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.resources.task_resources import TaskResource

task_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")
task_resource = TaskResource()


@task_bp.get("/")
@jwt_required()
def get_tasks():
    return task_resource.get()


@task_bp.post("/")
@jwt_required()
def create_task():
    return task_resource.post()
