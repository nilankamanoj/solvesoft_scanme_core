from functools import wraps

import flask_jwtlogin as jwt
from flask_jwtlogin import JWTLogin

from config import Configuration
from service import userService

login_manager = JWTLogin()


@login_manager.user_loader
def load_user(identifier):
    return userService.get_user(identifier)


def admin(f):
    if Configuration.AUTH_SKIP:
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)

        return decorated_function

    @wraps(f)
    @login_manager.jwt_required
    def decorated_function(*args, **kwargs):
        auth_user_role = jwt.current_user.role
        if auth_user_role != 0:
            return "unauthorized", 401
        return f(*args, **kwargs)

    return decorated_function


def privacy_officer(f):
    if Configuration.AUTH_SKIP:
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)

        return decorated_function

    @wraps(f)
    @login_manager.jwt_required
    def decorated_function(*args, **kwargs):
        auth_user_role = jwt.current_user.role
        if auth_user_role != 1:
            return "unauthorized", 401
        return f(*args, **kwargs)

    return decorated_function


def document_creator(f):
    if Configuration.AUTH_SKIP:
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)

        return decorated_function

    @wraps(f)
    @login_manager.jwt_required
    def decorated_function(*args, **kwargs):
        auth_user_role = jwt.current_user.role
        if auth_user_role != 2:
            return "unauthorized", 401
        return f(*args, **kwargs)

    return decorated_function


def privacy_officer_or_document_creator(f):
    if Configuration.AUTH_SKIP:
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)

        return decorated_function

    @wraps(f)
    @login_manager.jwt_required
    def decorated_function(*args, **kwargs):
        auth_user_role = jwt.current_user.role
        if auth_user_role != 1 and auth_user_role != 2:
            return "unauthorized", 401
        return f(*args, **kwargs)

    return decorated_function
