from flask import Blueprint
from app.resources.user_resources import UserResource

user_bp = Blueprint("users", __name__, url_prefix="")
user_resource = UserResource()


@user_bp.post("/register")
def register():
    return user_resource.register()


@user_bp.post("/login")
def login():
    return user_resource.login()
