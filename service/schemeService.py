import flask_jwtlogin as jwt

from model import db
from model.scheme import Scheme
from service import levelService


def save_scheme(scheme):
    s = Scheme(scheme['name'], jwt.current_user.id, scheme['description'], scheme['levels'])
    db.session.add(s)
    db.session.commit()
    for l in scheme['levels']:
        l['scheme_id'] = s.id
        levelService.save_level(l)
    return s


def get_schemes():
    schemes = Scheme.query.all()
    for scheme in schemes:
        scheme.levels = levelService.get_levels_by_scheme_id(scheme.id)
    return schemes


def get_scheme(id):
    scheme = Scheme.query.filter_by(id=id).first()
    scheme.levels = levelService.get_levels_by_scheme_id(scheme.id)
    return scheme


def get_scheme_by_name(name):
    scheme = Scheme.query.filter_by(name=name).first()
    if scheme is not None:
        scheme.levels = levelService.get_levels_by_scheme_id(scheme.id)
    return scheme
