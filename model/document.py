from model import db


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.ForeignKey(u'user.id', onupdate=u'CASCADE'), index=True)

    user = db.relationship(u'User')

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
