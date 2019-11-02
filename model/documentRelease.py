from model import db


class DocumentRelease(db.Model):
    __tablename__ = 'document_release'

    id = db.column(db.Integer(11), primary_key=True)
    level_id = db.column(db.ForeignKey(u'level.id', onupdate=u'CASCADE'), index=True)
    document_id = db.column(db.ForeignKey(u'document.id', onupdate=u'CASCADE'), index=True)
    created_time = db.column(db.Timestamp)

    document = db.relationship(u'Document')
    level = db.relationship(u'Level')