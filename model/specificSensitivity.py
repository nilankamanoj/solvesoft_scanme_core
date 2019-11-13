from model import db


class SpecificSensitivity(db.Model):
    __tablename__ = 'specific_sensitivity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    stream_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    stream = ''

    def serialize(self):
        return {
            'name': self.name,
            'stream_id': self.stream_id,
            'description': self.description,
            'id':self.id
        }
