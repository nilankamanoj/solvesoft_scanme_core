from model import db


class Stream(db.Model):
    __tablename__ = 'stream'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))

    specific_sensitivities = []

    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'specific_sensitivities': [s.serialize() for s in self.specific_sensitivities]
        }
