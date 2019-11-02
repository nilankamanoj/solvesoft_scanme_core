import os
import random
import string

from flask import Blueprint, request, jsonify, session

from config import Configuration
from service import fileService

file_controller = Blueprint('file_controller', __name__)


@file_controller.route('/', methods=['POST'])
def create_file():
    #################################################################
    # for dev purpose:
    session['uid'] = 1
    #################################################################
    document = request.form
    tmp_document = fileService.get_document_by_name(document['name'])
    if tmp_document is None:
        document = fileService.save_document(document)
        file = request.files['pdfFile']
        filename = random_string()
        file.save(os.path.join(Configuration.UPLOAD_FOLDER, filename + '.pdf'))
        return jsonify(
            {'data': fileService.extract_data(filename + '.pdf'), 'baseFileName': filename, 'version': 1,
             'documentId': document.id})
    else:
        return 'duplicate file name', 400


def random_string(string_length=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
