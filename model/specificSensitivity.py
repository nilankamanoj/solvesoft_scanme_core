from model import db


class SpecificSensitivity(db.Model):
    __tablename__ = 'specific_sensitivity'

    id = db.column(db.Integer(11), primary_key=True)
    name = db.column(db.String(50))
    stream_id = db.column(db.ForeignKey(u'stream.id', onupdate=u'CASCADE'), index=True)
    description = db.column(db.String(255))
    created_time = db.column(db.Timestamp)

    stream = db.relationship(u'Stream')