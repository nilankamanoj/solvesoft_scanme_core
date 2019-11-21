from model import db


class Level(db.Model):
    __tablename__ = 'level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    color = db.Column(db.String(255))
    scheme_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    is_party = db.Column(db.Boolean)

    include_level_id = None
    specific_sensitivities = []

    def __init__(self, name, color, scheme_id, description, is_party, include_level_id, specific_sensitivities):
        self.name = name
        self.color = color
        self.scheme_id = scheme_id
        self.description = description
        self.is_party = is_party
        self.include_level_id = include_level_id
        self.specific_sensitivities = specific_sensitivities

    def serialize(self):
        return {
            'id':self.id,
            'name': self.name,
            'color': 'rgb('+self.color+')',
            'description': self.description,
            'is_party': self.is_party,
            'include_level_id': self.include_level_id,
            'specific_sensitivities': [s.serialize() for s in self.specific_sensitivities]
        }
