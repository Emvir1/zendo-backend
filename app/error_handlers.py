from marshmallow import ValidationError
from app.extensions import jwt_manager


def register_error_handlers(app):

    # ── HTTP error handlers ──────────────────────────────────────────────────

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return {"errors": e.messages}, 422

    @app.errorhandler(400)
    def bad_request(e):
        return {"message": "Bad request"}, 400

    @app.errorhandler(401)
    def unauthorized(e):
        return {"message": "Unauthorized"}, 401

    @app.errorhandler(403)
    def forbidden(e):
        return {"message": "Forbidden"}, 403

    @app.errorhandler(404)
    def not_found(e):
        return {"message": "Resource not found"}, 404

    @app.errorhandler(500)
    def internal_error(e):
        return {"message": "Internal server error"}, 500

    # ── JWT error handlers (override Flask-JWT-Extended defaults) ────────────

    @jwt_manager.unauthorized_loader
    def missing_token(reason):
        return {"message": "Unauthorized"}, 401

    @jwt_manager.invalid_token_loader
    def invalid_token(reason):
        return {"message": "Invalid token"}, 401

    @jwt_manager.expired_token_loader
    def expired_token(jwt_header, jwt_data):
        return {"message": "Session expired, please log in again"}, 401

    @jwt_manager.revoked_token_loader
    def revoked_token(jwt_header, jwt_data):
        return {"message": "Token has been revoked"}, 401
