from model import db
from model.violation import Violation
from service.releaseService import get_release


def get_all_violations():
    vs = []
    for v in Violation.query.all():
        v.release = get_release(v.release_id)
        vs.append(v)
    return vs


def create_violation(v):
    db.session.add(v)
    db.session.commit()
    return v
