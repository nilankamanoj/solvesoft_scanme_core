from flask import Flask, render_template
from flask_restful import reqparse

from config import Configuration
from controller import login_manager
from controller.fileController import file_controller
from controller.schemeController import scheme_controller
from controller.streamController import stream_controller
from controller.userController import user_controller
from controller.violationController import violation_controller
from controller.noteController import note_controller
from model import db

app = Flask(__name__, static_url_path='', template_folder='frontend', static_folder='frontend')
app.config.from_object(Configuration)
db.init_app(app)
login_manager.init_app(app)
parser = reqparse.RequestParser()
parser.add_argument('pdfFile')

app.register_blueprint(user_controller, url_prefix='/user')
app.register_blueprint(file_controller, url_prefix='/file')
app.register_blueprint(stream_controller, url_prefix='/stream')
app.register_blueprint(scheme_controller, url_prefix='/scheme')
app.register_blueprint(violation_controller, url_prefix='/violation')
app.register_blueprint(note_controller, url_prefix='/note')


@app.route('/')
def projects():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
