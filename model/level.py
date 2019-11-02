from model import db


class Level(db.Model):
    __tablename__ = 'level'

    id = db.column(db.Integer(11), primary_key=True)
    name = db.column(db.String(255))
    color = db.Column(db.String(255))
    scheme_id = db.column(db.ForeignKey(u'scheme.id', onupdate=u'CASCADE'), index=True)
    description = db.column(db.String(255))
    is_party = db.column(db.Boolean)
    created_time = db.column(db.Timestamp)

    scheme = db.relationship(u'Scheme')