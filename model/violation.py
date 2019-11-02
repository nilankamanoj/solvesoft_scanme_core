from model import db


class Violation(db.Model):
    __tablename__ = 'violation'

    id = db.column(db.Integer(11), primary_key=True)
    release_id = db.column(db.ForeignKey(u'document_release.id', onupdate=u'CASCADE'), index=True)
    description = db.column(db.String(255))
    created_time = db.column(db.Timestamp)

    release = db.relationship(u'DocumentRelease')
