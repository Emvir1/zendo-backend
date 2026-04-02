from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError
from app.services.task_services import get_all_tasks, create_task
from app.validations.task_validations import TaskSchema


class TaskResource:
    schema = TaskSchema()

    def get(self):
        tasks = get_all_tasks()
        return jsonify({"tasks": tasks}), 200

    def post(self):
        try:
            data = self.schema.load(request.get_json() or {})
        except ValidationError as e:
            return jsonify({"errors": e.messages}), 422

        data["user_id"] = get_jwt_identity()
        task = create_task(data)
        return jsonify({"task": task}), 201
