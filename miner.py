import fitz
import werkzeug
import os
from flask import Flask, request, send_from_directory
from flask_restful import reqparse, Api, Resource
from os.path import dirname, realpath

UPLOAD_FOLDER = dirname(realpath(__file__)) + '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('pdfFile')


def textHighlight(filename):
    doc = fitz.open(UPLOAD_FOLDER + "/" + filename)
    page = doc[0]

    text = "more"
    text_instances = page.searchFor(text)

    ### HIGHLIGHT

    for inst in text_instances:
        highlight = page.addHighlightAnnot(inst)
        highlight.setColors({"stroke": (1, 0, 0), "fill": (0.75, 0.8, 0.95)})
        highlight.update()

    doc.save(os.path.join(app.config['UPLOAD_FOLDER'], 'highlighted.pdf'))

    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename='highlighted.pdf')


class pdfTextHighlighter(Resource):
    def post(self):
        file = request.files['pdfFile']
        filename = werkzeug.secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return textHighlight(filename)


api.add_resource(pdfTextHighlighter, '/textHighlight')

if __name__ == '__main__':
    app.run(debug=True)
