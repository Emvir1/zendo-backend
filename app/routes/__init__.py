from flask import Blueprint
from app.routes.auth_routes import auth_bp
from app.routes.task_routes import task_bp
from app.routes.user_routes import user_bp

index_bp = Blueprint("index", __name__)


@index_bp.get("/")
def index():
    return {"message": "ZenDo API is running", "status": "ok"}, 200


all_blueprints = [
    index_bp,
    auth_bp,
    task_bp,
    user_bp,
]


def register_blueprints(app):
    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)
