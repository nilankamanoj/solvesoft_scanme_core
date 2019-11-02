from model import db
from model.party import Party


def save_party_include_level(party):
    p = Party(party['party_level_id'], party['include_level_id'])
    db.session.add(p)
    db.session.commit()
    return p


def get_include_party_by_party_level_id(party_level_id):
    return Party.query.filter_by(party_level_id=party_level_id).first()
