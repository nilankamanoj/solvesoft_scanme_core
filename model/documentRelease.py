from model import db


class DocumentRelease(db.Model):
    __tablename__ = 'document_release'

    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer)
    document_id = db.Column(db.Integer)
    doc_name = ""
    level_name = ""
    user_name = ""

    def __init__(self, level_id, document_id):
        self.level_id = level_id
        self.document_id = document_id
