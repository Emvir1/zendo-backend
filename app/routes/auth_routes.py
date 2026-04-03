from flask import Blueprint
from app.resources.auth_resources import AuthResource

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_resource = AuthResource()


@auth_bp.post("/register")
def register():
    return auth_resource.register()


@auth_bp.post("/login")
def login():
    return auth_resource.login()
