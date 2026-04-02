from flask import Flask
from app.extensions import db, migrate, jwt_manager, cors


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt_manager.init_app(app)
    cors.init_app(app)

    with app.app_context():
        from app.models import user_model, task_model  # noqa: F401

        from app.routes.task_routes import task_bp
        from app.routes.user_routes import user_bp
        app.register_blueprint(task_bp)
        app.register_blueprint(user_bp)

    return app
