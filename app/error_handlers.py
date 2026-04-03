from marshmallow import ValidationError


def register_error_handlers(app):

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
