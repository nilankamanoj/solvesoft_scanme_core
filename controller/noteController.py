from flask import Blueprint
from flask import request, json, jsonify
import flask_jwtlogin as jwt

from controller import admin, login_manager, user
from service import noteService

note_controller = Blueprint('note_controller', __name__)


@note_controller.route("/", methods=['GET'])
def get_all():
    return jsonify([n.serialize() for n in noteService.get_notes()])


@note_controller.route("/<int:id>", methods=['GET'])
def get_one(id):
    n = noteService.get_note(id)
    if n is not None:
        return jsonify(n.serialize())
    return 'note not found', 400

@note_controller.route("/userid/<int:id>", methods=['GET'])
def get_notes_by_userid(user_id):
    n = noteService.get_note_by_user_id(user_id)
    if n is not None:
        return jsonify(n.serialize())
    return 'note not found', 400




@note_controller.route("/", methods=['POST'])
def add():
    note = json.loads(request.data.decode('utf-8'))
    n = noteService.save_note(note)
    if n is None:
        return jsonify(noteService.save_note(note).serialize())
    return 'duplicate email', 400



