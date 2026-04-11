from http import HTTPStatus
from app.extensions import db
from app.models.list_model import List


def create_list(data):
    new_list = List(
        category=data.get("category"),
        user_id=int(data["user_id"]),
    )

    db.session.add(new_list)
    db.session.commit()

    return new_list.get_list(), HTTPStatus.CREATED

def get_all_lists(user_id):
    lists = List.query.filter_by(user_id=int(user_id)).all()
    return [lst.all_lists() for lst in lists], HTTPStatus.OK

def get_list_by_id(list_id, user_id):
    lst = List.query.filter_by(id=list_id, user_id=int(user_id)).first()
    if not lst:
        return None, HTTPStatus.NOT_FOUND
    return lst.get_list(), HTTPStatus.OK

def update_list(list_id, user_id, data):
    lst = List.query.filter_by(id=list_id, user_id=int(user_id)).first()
    if not lst:
        return None, HTTPStatus.NOT_FOUND

    if data.get("category") is not None:
        lst.category = data["category"]

    db.session.commit()
    return lst.get_list(), HTTPStatus.OK

def delete_list(list_id, user_id):
    lst = List.query.filter_by(id=list_id, user_id=int(user_id)).first()
    if not lst:
        return None, HTTPStatus.NOT_FOUND

    db.session.delete(lst)
    db.session.commit()
    return None, HTTPStatus.OK

