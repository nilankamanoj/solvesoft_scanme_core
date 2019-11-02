from model import db


class Party(db.Model):
    __tablename__ = 'party'
    
    id = db.Column(db.Integer, primary_key=True)
    party_level_id = db.Column(db.Integer)
    include_level_id = db.Column(db.Integer)

    def __init__(self, party_level_id, include_level_id):
        self.party_level_id = party_level_id
        self.include_level_id = include_level_id



