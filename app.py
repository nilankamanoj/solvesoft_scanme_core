from flask import Flask, jsonify
from flask_restful import reqparse

from config import Configuration
from controller import login_manager
from controller.fileController import file_controller
from controller.schemeController import scheme_controller
from controller.streamController import stream_controller
from controller.userController import user_controller
from model import db

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
login_manager.init_app(app)
parser = reqparse.RequestParser()
parser.add_argument('pdfFile')

app.register_blueprint(user_controller, url_prefix='/user')
app.register_blueprint(file_controller, url_prefix='/file')
app.register_blueprint(stream_controller, url_prefix='/stream')
app.register_blueprint(scheme_controller, url_prefix='/scheme')


@app.route('/')
def hello_world():
    return jsonify({'user': '/user', 'file': '/file'})


if __name__ == '__main__':
    app.run()
