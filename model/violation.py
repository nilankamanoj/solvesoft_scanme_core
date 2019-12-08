from model import db


class Violation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    release_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    checked = db.Column(db.Boolean)
    created_time = db.Column(db.TIMESTAMP)
    release = None

    def _init_(self, release_id, description, checked):
        self.release_id = release_id
        self.description = description
        self.checked = checked

    def serialize(self):
        return {
            'id':self.id,
            'release_id':self.release_id,
            'description':self.description,
            'cheked':self.checked,
            'created_time':self.created_time,
            'release': self.release.serialize()
        }
