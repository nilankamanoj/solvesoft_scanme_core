from flask import Blueprint
from flask import request, json, jsonify

from controller import login_manager
from service import userService

user_controller = Blueprint('user_controller', __name__)


@user_controller.route("/", methods=['GET'])
@login_manager.jwt_required
def get_all():
    return jsonify([u.serialize() for u in userService.get_users()])


@user_controller.route("/<int:id>", methods=['GET'])
def get_one(id):
    u = userService.get_user(id)
    if u is not None:
        return jsonify(u.serialize())
    return 'user not found', 400


@user_controller.route("/", methods=['POST'])
def add():
    user = json.loads(request.data.decode('utf-8'))
    return jsonify(userService.save_user(user).serialize())


@user_controller.route('/login', methods=['POST'])
def get_token():
    login_user = userService.login(request.form)
    if login_user is not None:
        return jsonify(login_manager.generate_jwt_token(login_user.id))
    else:
        return 'bad credentials', 401
