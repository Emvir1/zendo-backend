from flask import Flask
from app.extensions import db, migrate, jwt_manager, cors
from app.error_handlers import register_error_handlers
from app.routes import register_blueprints


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt_manager.init_app(app)
    cors.init_app(app)

    register_error_handlers(app)
    register_blueprints(app)

    return app
