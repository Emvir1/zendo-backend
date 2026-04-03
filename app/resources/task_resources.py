from flask import request
from flask_jwt_extended import get_jwt_identity
from app.services import task_services
from app.validations.task_validations import TaskSchema


class TaskResource:

    def get(self):
        tasks, message, status_code = task_services.get_all_tasks()
        return {"message": message, "tasks": tasks}, status_code

    def post(self):
        schema = TaskSchema()
        data = schema.load(request.get_json())
        data["user_id"] = get_jwt_identity()
        task, message, status_code = task_services.create_task(data)
        return {"message": message, "task": task}, status_code
