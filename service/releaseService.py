from model import db
from model.documentRelease import DocumentRelease
from service.fileService import get_document


def get_releases():
    return DocumentRelease.query.all()


def get_release(id):
    r = DocumentRelease.query.filter_by(id=id).first()
    document = get_document(r.document_id)


def save_release(r):
    db.session.add(r)
    db.session.commit()
    return r
