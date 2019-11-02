from model import db


class Scheme(db.Model):
    __tablename__ = 'scheme'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    description = db.Column(db.String(255))

    levels = []

    def __init__(self, name, user_id, description, levels):
        self.name = name
        self.user_id = user_id
        self.description = description
        self.levels = levels

    def serialize(self):
        return {
            'name': self.name,
            'user_id': self.user_id,
            'description': self.description,
            'levels': [l.serialize() for l in self.levels]
        }
