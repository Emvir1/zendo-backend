from flask import request
from flask_jwt_extended import get_jwt_identity
from app.services import list_services

class ListResource:
    """Handles /api/lists/ — collection endpoints."""

    def get(self):
        user_id = get_jwt_identity()
        lists, status_code = list_services.get_all_lists(user_id)
        return {"lists": lists}, status_code

    def post(self):
        data = request.get_json()
        data["user_id"] = get_jwt_identity()
        list_, status_code = list_services.create_list(data)
        return {"message": "List created successfully", "list": list_}, status_code

class ListDetailResource:
    """Handles /api/lists/<id> — single list endpoints."""

    def get(self, list_id):
        user_id = get_jwt_identity()
        list_, status_code = list_services.get_list_by_id(list_id, user_id)
        if status_code != 200:
            return {"message": "List not found"}, status_code
        return {"list": list_}, status_code

    def patch(self, list_id):
        data = request.get_json()
        user_id = get_jwt_identity()
        list_, status_code = list_services.update_list(list_id, user_id, data)

        if not list_:
            return {"message": "List not found"}, status_code
            
        return {"message": "List updated successfully", "list": list_}, status_code

    def delete(self, list_id):
        user_id = get_jwt_identity()
        _, status_code = list_services.delete_list(list_id, user_id)
        return {"message": "List deleted successfully"}, status_code
