import os
import random
import string

from flask import Blueprint, request, jsonify, session, json, send_from_directory

from config import Configuration
from controller import document_creator
from service import fileService, schemeService
from util.fileUtil import highlight_pdf

file_controller = Blueprint('file_controller', __name__)


@file_controller.route('/', methods=['POST'])
@document_creator
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
        data = {'data': fileService.extract_data(filename + '.pdf'), 'baseFileName': filename, 'version': 1,
                'documentId': document.id, 'scheme': ''}
        return jsonify(data)
    return 'duplicate file name', 400


@file_controller.route('/highlight', methods=['POST'])
@document_creator
def highlight():
    data = json.loads(request.data.decode('utf-8'))
    scheme = schemeService.get_scheme_by_name(data['scheme'])
    highlight_pdf(data, scheme)
    return send_from_directory(Configuration.UPLOAD_FOLDER, data['baseFileName'] + str(data['version']) + '.pdf')


def random_string(string_length=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
