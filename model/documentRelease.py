from model import db


class DocumentRelease(db.Model):
    __tablename__ = 'document_release'

    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer)
    document_id = db.Column(db.Integer)
    doc_name = ""
    user_name = ""
    level = ""

    def __init__(self, level_id, document_id):
        self.level_id = level_id
        self.document_id = document_id

    def serialize(self):
        return{
            'doc_name':self.doc_name,
            'user_name':self.user_name,
            'level':self.level
        }


