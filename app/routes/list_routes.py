from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.resources.list_resources import ListResource, ListDetailResource


list_bp = Blueprint("lists", __name__, url_prefix="/api/lists")
list_resource = ListResource()
list_detail_resource = ListDetailResource()


@list_bp.post("/")
@jwt_required()
def create_lists():
    return list_resource.post()

@list_bp.get("/")
@jwt_required()
def get_lists():
    return list_resource.get()

@list_bp.get("/<int:list_id>")
@jwt_required()
def get_list_by_id(list_id):
    return list_detail_resource.get(list_id)

@list_bp.patch("/<int:list_id>")
@jwt_required()
def update_list(list_id):
    return list_detail_resource.patch(list_id)

@list_bp.delete("/<int:list_id>")
@jwt_required()
def delete_list(list_id):
    return list_detail_resource.delete(list_id)