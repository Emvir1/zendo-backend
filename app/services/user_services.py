from app.extensions import db
from app.models.user_model import User


def get_user_by_id(user_id):
    user = db.session.get(User, int(user_id))
    if not user:
        return None, "User not found", 404
    return user.get_user(), "User retrieved successfully", 200


def update_user(user_id, data):
    user = db.session.get(User, user_id)
    if not user:
        return None, "User not found", 404

    if data.get("username") and data["username"] != user.username:
        existing = User.query.filter_by(username=data["username"]).first()
        if existing:
            return None, "Username already taken", 409

    for key, value in data.items():
        if value is not None:
            setattr(user, key, value)

    db.session.commit()
    return user.get_user(), "User updated successfully", 200
