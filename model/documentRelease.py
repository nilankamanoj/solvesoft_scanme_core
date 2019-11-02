from model import db


class DocumentRelease(db.Model):
    __tablename__ = 'document_release'

    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer)
    document_id = db.Column(db.Integer)
