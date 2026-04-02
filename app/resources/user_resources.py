from flask import jsonify, request, make_response
from marshmallow import ValidationError
from app.services.user_services import register_user, login_user
from app.validations.user_validations import RegisterSchema, LoginSchema


class UserResource:
    register_schema = RegisterSchema()
    login_schema = LoginSchema()

    def register(self):
        try:
            data = self.register_schema.load(request.get_json() or {})
        except ValidationError as e:
            return jsonify({"errors": e.messages}), 422

        user, errors = register_user(data)
        if errors:
            return jsonify({"errors": errors}), 409

        return jsonify({"user": user}), 201

    def login(self):
        try:
            data = self.login_schema.load(request.get_json() or {})
        except ValidationError as e:
            return jsonify({"errors": e.messages}), 422

        result, errors = login_user(data)
        if errors:
            return jsonify(errors), 401

        response = make_response(jsonify({"user": result["user"]}), 200)
        response.set_cookie("access_token_cookie", result["access_token_cookie"])
        response.set_cookie("csrf_access_token", result["csrf_access_token"])

        return response
