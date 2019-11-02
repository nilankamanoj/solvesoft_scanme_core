from flask_jwtlogin import JWTLogin

from service import userService

login_manager = JWTLogin()


@login_manager.user_loader
def load_user(identifier):
    return userService.get_user(identifier)
