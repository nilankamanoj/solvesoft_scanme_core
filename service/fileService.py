import fitz
import flask_jwtlogin as jwt
import nltk

from config import Configuration
from model import db
from model.document import Document
from util.scanUtil import get_human_names

tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')


def extract_data(filename):
    doc = fitz.open(Configuration.UPLOAD_FOLDER + "/" + filename)
    data = []
    page_num = 0

    for page in doc:
        data.append({"page": page_num, "sentences": [], "telephones": [], "emails": [], "nics": []})
        all_text = page.getText()
        sentences = tokenizer.tokenize(all_text)
        sentence_num = 0
        for sentence in sentences:
            person_names = get_human_names(sentence)

            if len(person_names) > 0:
                data[page_num].get("sentences").append(
                    {"id": str(page_num) + str(sentence_num), "text": sentence,
                     "names": [{"checked": True, "data": pn} for pn in person_names], "stream": "",
                     "spec": "", "checked": True})
            sentence_num += 1
        page_num += 1

    return data


def get_documents():
    return Document.query.all()


def get_document(id):
    return Document.query.filter_by(id=id).first()


def get_document_by_name(name):
    return Document.query.filter_by(name=name).first()


def save_document(document):
    d = Document(document['name'], jwt.current_user.id)
    db.session.add(d)
    db.session.commit()
    return d
