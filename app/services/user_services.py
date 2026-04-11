from http import HTTPStatus
from app.extensions import db
from app.models.user_model import User


def get_user_by_id(user_id):
    user = db.session.get(User, int(user_id))
    if not user:
        return None, "User not found", HTTPStatus.NOT_FOUND
    return user.get_user(), HTTPStatus.OK


def update_user(user_id, data):
    user = db.session.get(User, user_id)
    if not user:
        return None, "User not found", HTTPStatus.NOT_FOUND

    if data.get("username") and data["username"] != user.username:
        existing = User.query.filter_by(username=data["username"]).first()
        if existing:
            return None, "Username already taken", HTTPStatus.CONFLICT

    for key, value in data.items():
        if value is not None:
            setattr(user, key, value)

    db.session.commit()
    return user.get_user(), HTTPStatus.OK
