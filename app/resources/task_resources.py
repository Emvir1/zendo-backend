from http import HTTPStatus
from flask import request
from flask_jwt_extended import get_jwt_identity
from app.services import task_services
from app.validations.task_validations import TaskSchema, TaskUpdateSchema


class TaskResource:
    """Handles /api/tasks/ — collection endpoints."""

    def get(self):
        user_id = get_jwt_identity()
        tasks, status_code = task_services.get_all_tasks(user_id)
        return {"tasks": tasks}, status_code

    def post(self):
        schema = TaskSchema()
        data = schema.load(request.get_json())
        data["user_id"] = get_jwt_identity()
        task, status_code = task_services.create_task(data)
        if status_code != HTTPStatus.CREATED:
            return task, status_code
        return {"message": "Task created successfully", "task": task}, status_code


class TaskDetailResource:
    """Handles /api/tasks/<id> — single task endpoints."""

    def get(self, task_id):
        user_id = get_jwt_identity()
        task, status_code = task_services.get_task_by_id(task_id, user_id)
        if status_code == HTTPStatus.NOT_FOUND:
            return {"message": "Task not found"}, status_code
        return {"task": task}, status_code

    def patch(self, task_id):
        schema = TaskUpdateSchema()
        data = schema.load(request.get_json())
        user_id = get_jwt_identity()
        task, status_code = task_services.update_task(task_id, user_id, data)

        if not task:
            return {"message": "Task not found"}, status_code

        return {"message": "Task updated successfully", "task": task}, status_code

    def delete(self, task_id):
        user_id = get_jwt_identity()
        _, status_code = task_services.delete_task(task_id, user_id)

        if status_code == HTTPStatus.NOT_FOUND:
            return {"message": "Task not found"}, status_code

        return {"message": "Task deleted successfully"}, status_code
