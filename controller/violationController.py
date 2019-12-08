from flask import Blueprint
from flask import jsonify

from service import violationService
from controller import privacy_officer
violation_controller = Blueprint('violation_controller', __name__)

@violation_controller.route("/",methods=['GET'])
def get_all():
    return jsonify([s.serialize() for s in violationService.get_all_violations()])