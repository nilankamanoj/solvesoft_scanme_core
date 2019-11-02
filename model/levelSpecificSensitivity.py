from model import db


class LevelSpecificSensitivity(db.Model):
    __tablename__ = 'level_specific_sensitivity'

    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer)
    specific_sensitivity_id = db.Column(db.Integer)

    def __init__(self, level_id, specific_sensitivity_id):
        self.level_id = level_id
        self.specific_sensitivity_id = specific_sensitivity_id

    def serialize(self):
        return {
            'level_id': self.level_id,
            'specific_sensitivity_id': self.specific_sensitivity_id
        }
