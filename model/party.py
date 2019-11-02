from model import db


class Party(db.Model):
    __tablename__ = 'party'
    
    id = db.column(db.Integer(11), primary_key=True)
    party_level_id = db.column(db.ForeignKey(u'level.id', onupdate=u'CASCADE'))
    include_level_id = db.column(db.ForeignKey(u'level.id', onupdate=u'CASCADE'), index=True)
    created_time = db.column(db.Timestamp)

    include_level = db.relationship(u'Level', primaryjoin='Party.include_level_id == Level.id')
    party_level = db.relationship(u'Level', primaryjoin='Party.party_level_id == Level.id')
