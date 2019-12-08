from model import db


class Violation(db.Model):
    __tablename__ = 'violation'

    id = db.Column(db.Integer, primary_key=True)
    release_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    checked = db.Column(db.Boolean)
    created_time = db.Column(db.TIMESTAMP)

    def _init_(self, release_id, description, checked, created_time):
        self.release_id = release_id
        self.description = description
        self.checked = checked
        self.created_time = created_time
    
    def serialize(self):
        return {
            'id':self.id,
            'release_id':self.release_id,
            'description':self.description,
            'cheked':self.checked,
            'created_time':self.created_time
        }
