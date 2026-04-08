from flask import request
from flask_jwt_extended import get_jwt_identity
from app.services import user_services
from app.validations.user_validations import UserSchema


class UserListResource:

    def get(self):
        user_id = get_jwt_identity()
        user, message, status_code = user_services.get_user_by_id(user_id)
        if status_code != 200:
            return {"message": message}, status_code
        return {"user": user}, status_code


class UserDetailResource:
    
    def patch(self):
        user_id = get_jwt_identity()
        schema = UserSchema()
        data = schema.load(request.get_json(), partial=True)
        user, message, status_code = user_services.update_user(user_id, data)
        if status_code != 200:
            return {"message": message}, status_code
        return {"message": message, "user": user}, status_code
    