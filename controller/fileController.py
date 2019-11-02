import os

import werkzeug
from flask import Blueprint, request, jsonify

from config import Configuration
from service import fileService

file_controller = Blueprint('file_controller', __name__)


@file_controller.route('/', methods=['POST'])
def create_file():
    file = request.files['pdfFile']
    filename = werkzeug.secure_filename(file.filename)
    file.save(os.path.join(Configuration.UPLOAD_FOLDER, filename))
    return jsonify(fileService.extract_data(filename))
