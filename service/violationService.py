from model import db
from model.violation import Violation

def get_all_violations():
    return Violation.query.all()