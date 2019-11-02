from model import db


class Scheme(db.Model):
    __tablename__ = 'scheme'

    id = db.column(db.Integer(11), primary_key=True)
    name = db.column(db.String(255))
    user_id = db.column(db.ForeignKey(u'user.id', onupdate=u'CASCADE'), index=True)
    description = db.column(db.String(255))
    created_time = db.column(db.Timestamp)

    user = db.relationship(u'User')