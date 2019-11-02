from model import db


class Violation(db.Model):
    __tablename__ = 'violation'

    id = db.Column(db.Integer, primary_key=True)
    release_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
