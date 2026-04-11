from flask import request, make_response
from flask_jwt_extended import set_access_cookies
from app.services import auth_services
from app.validations.auth_validations import RegisterSchema, LoginSchema


class AuthResource:

    def register(self):
        schema = RegisterSchema()
        data = schema.load(request.get_json())
        _, status_code = auth_services.register_user(data)
        return {"message": "User registered successfully"}, status_code

    def login(self):
        schema = LoginSchema()
        data = schema.load(request.get_json())
        result, status_code = auth_services.login_user(data)
        if status_code != 200:
            return {"message": "Invalid username or password"}, status_code

        response = make_response(
            {"message": "Login successful", "user": result["user"], "access_token_cookie": result["access_token_cookie"]},
            status_code
        )
        set_access_cookies(response, result["access_token_cookie"])
        return response
