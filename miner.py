import fitz
import werkzeug
import os
from flask import Flask, request, send_from_directory
from flask_restful import reqparse, Api, Resource
from os.path import dirname, realpath
from string import punctuation
from nltk.corpus import stopwords
import json
import * from personnameTest
# https://pymupdf.readthedocs.io/en/latest/rect/

UPLOAD_FOLDER = dirname(realpath(__file__)) + '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('pdfFile')

    

def textHighlight(filename):
    doc = fitz.open(UPLOAD_FOLDER + "/" + filename)

    coordinationArray = []
    pageNum = 0

    for page in doc:
        allText = page.getText()

        # puncRemovedText = " ".join(removePunctuation(i) for i in allText.split())
        # stopWordsRemovedTextList = removeStopWords(puncRemovedText.split())
        # cleanedText = removeNumbers(stopWordsRemovedTextList)
        # uniqueWords = list(set(cleanedText))
        personNames = get_human_names(allText)

        textCoordinateArray = []

        # for word in uniqueWords:
        #     text_instances = page.searchFor(word, 30, False)
        #     textCoordinateArray.append({"word": word, "coordinates": text_instances})
        # pageNum += 1
        # coordinationArray.append({"page": pageNum, "wordsWithCoordinates": textCoordinateArray})
        for personName in personNames:
            text_instances = page.searchFor(personName, 30, False)

    ### HIGHLIGHT

            for inst in text_instances:
                highlight = page.addHighlightAnnot(inst)
                highlight.setColors({"stroke": (1, 0, 0), "fill": (102/255, 224/255, 255/255)})
                highlight.update()
    #
    doc.save(os.path.join(app.config['UPLOAD_FOLDER'], 'highlighted.pdf'))

    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename='highlighted.pdf')
    # return {'success': 'true'}


def removePunctuation(strval):
    return "".join(" " if i in punctuation else i for i in strval.strip(punctuation))


def removeStopWords(word_list):
    filtered_words = [word for word in word_list if word.lower() not in stopwords.words('english')]
    return filtered_words


def removeNumbers(word_list):
    return [word for word in word_list if word.isdigit() != True]


class pdfTextHighlighter(Resource):
    def post(self):
        file = request.files['pdfFile']
        filename = werkzeug.secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return textHighlight(filename)


api.add_resource(pdfTextHighlighter, '/textHighlight')

if __name__ == '__main__':
    app.run(debug=True)
