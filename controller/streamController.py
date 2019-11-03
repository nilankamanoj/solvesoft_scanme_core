from flask import Blueprint
from flask import jsonify

from service import streamService
from controller import privacy_officer
stream_controller = Blueprint('stream_controller', __name__)


@stream_controller.route("/", methods=['GET'])
@privacy_officer
def get_all():
    return jsonify([s.serialize() for s in streamService.get_streams()])
