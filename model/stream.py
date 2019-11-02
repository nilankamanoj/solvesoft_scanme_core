from model import db


class Stream(db.Model):
    __tablename__ = 'stream'

    id = db.column(db.Integer(11), primary_key=True)
    name = db.column(db.String(50))
    description = db.column(db.String(255))
    created_time = db.column(db.Timestamp)
