from model import db
from model.note import Note


def get_notes():
    return Note.query.all()


def get_note(id):
    return Note.query.filter_by(id=id).first()


def save_note(note):
    n = Note(note['title'], note['content'], user['user_id'])
    db.session.add(n)
    db.session.commit()
    return u

def get_note_by_user_id(user_id):
    note = Note.query.filter_by(user_id=user_id).first()
    return note



