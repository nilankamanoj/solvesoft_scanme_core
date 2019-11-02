from flask import Blueprint
from flask import request, json, jsonify

from service import schemeService

scheme_controller = Blueprint('scheme_controller', __name__)


@scheme_controller.route("/", methods=['POST'])
def save_scheme():
    s = json.loads(request.data.decode('utf-8'))
    if schemeService.get_scheme_by_name(s['name']) is None:
        scheme = schemeService.save_scheme(s)
        return jsonify(schemeService.get_scheme(scheme.id).serialize())
    else:
        return "duplicate scheme name", 400


@scheme_controller.route("/", methods=['GET'])
def get_schemes():
    return jsonify([s.serialize() for s in schemeService.get_schemes()])
