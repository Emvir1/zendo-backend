from flask import request
from flask_jwt_extended import get_jwt_identity
from app.services import task_services
from app.validations.task_validations import TaskSchema, TaskUpdateSchema


class TaskResource:

    def get_all(self):
        user_id = get_jwt_identity()
        tasks, status_code = task_services.get_all_tasks(user_id)
        return {"tasks": tasks}, status_code

    def get_one(self, task_id):
        user_id = get_jwt_identity()
        task, message, status_code = task_services.get_task_by_id(task_id, user_id)
        if status_code != 200:
            return {"message": message}, status_code
        return {"task": task}, status_code

    def post(self):
        schema = TaskSchema()
        data = schema.load(request.get_json())
        data["user_id"] = get_jwt_identity()
        task, message, status_code = task_services.create_task(data)
        return {"message": message, "task": task}, status_code

    def patch(self, task_id):
        schema = TaskUpdateSchema()
        data = schema.load(request.get_json())
        user_id = get_jwt_identity()
        task, message, status_code = task_services.update_task(task_id, user_id, data)
        return {"message": message, "task": task}, status_code

    def delete(self, task_id):
        user_id = get_jwt_identity()
        _, message, status_code = task_services.delete_task(task_id, user_id)
        return {"message": message}, status_code