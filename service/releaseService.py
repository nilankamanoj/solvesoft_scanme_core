from model import db
from model.documentRelease import DocumentRelease
from service.fileService import get_document
from service.userService import get_user
from service.levelService import get_level


def get_releases():
    return DocumentRelease.query.all()


def get_release(id):
    r = DocumentRelease.query.filter_by(id=id).first()
    document = get_document(r.document_id)
    r.doc_name = document.name
    user = get_user(document.user_id)
    r.user_name = user.name
    level = get_level(r.level_id)
    r.level= level.name
    return r


def save_release(r):
    db.session.add(r)
    db.session.commit()
    return r
