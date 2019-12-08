from passlib.hash import pbkdf2_sha256 as sha256

from model import db


class Note(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
   
    
    def __init__(self, title):
        self.title = title
        self.content = content
        

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            
        }

    def is_anonymous(self):
        return False

    