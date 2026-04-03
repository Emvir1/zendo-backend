from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.extensions import db
from app.models.user_model import User


def register_user(data):
    existing = User.query.filter_by(username=data["username"]).first()
    if existing:
        return None, "Username already taken", 409

    user = User(
        username=data["username"],
        password=generate_password_hash(data["password"]),
        first_name=data["first_name"],
        last_name=data["last_name"],
        middle_name=data.get("middle_name"),
        birth_date=data.get("birth_date"),
        gender=data.get("gender"),
    )
    db.session.add(user)
    db.session.commit()
    return user.get_user(), "User registered successfully", 201


def login_user(data):
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return None, "Invalid username or password", 401

    access_token = create_access_token(identity=str(user.id))
    return {"access_token": access_token, "user": user.get_user()}, "Login successful", 200
