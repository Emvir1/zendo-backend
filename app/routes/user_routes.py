from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.resources.user_resources import UserResource, UserDetailResource

user_bp = Blueprint("users", __name__, url_prefix="/api/users")
user_list = UserResource()
user_detail = UserDetailResource()


@user_bp.get("/self")
@jwt_required()
def get_user():
    return user_list.get()


@user_bp.patch("/self")
@jwt_required()
def update_user():
    return user_detail.patch()
