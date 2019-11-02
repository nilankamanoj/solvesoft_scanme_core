from model import db
from model.user import User


def get_users():
    return User.query.all()


def get_user(id):
    return User.query.filter_by(id=id).first()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def save_user(user):
    u = User(user['name'], user['email'], user['password'], user['role'], user['is_enabled'])
    db.session.add(u)
    db.session.commit()
    return u


def login(user):
    u = get_user_by_email(user['email'])
    if u is not None and User.verify_hash(user['password'], u.password):
        return u
    else:
        return None
