from flask import Blueprint
from flask import request, json, jsonify

from controller import admin, login_manager
from service import userService

user_controller = Blueprint('user_controller', __name__)


@user_controller.route("/", methods=['GET'])
@admin
def get_all():
    return jsonify([u.serialize() for u in userService.get_users()])


@user_controller.route("/<int:id>", methods=['GET'])
@admin
def get_one(id):
    u = userService.get_user(id)
    if u is not None:
        return jsonify(u.serialize())
    return 'user not found', 400


@user_controller.route("/", methods=['POST'])
@admin
def add():
    user = json.loads(request.data.decode('utf-8'))
    u = userService.get_user_by_email(user['email'])
    if u is None:
        return jsonify(userService.save_user(user).serialize())
    return 'duplicate email', 400


@user_controller.route('/login', methods=['POST'])
def get_token():
    login_user = userService.login(request.form)
    if login_user is not None:
        return jsonify(login_manager.generate_jwt_token(login_user.id))
    return 'bad credentials', 401
