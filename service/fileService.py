import fitz
import nltk

from config import Configuration
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
                    {"id": str(page_num) + str(sentence_num), "text": sentence, "names": person_names, "stream": "",
                     "spec": ""})

                for personName in person_names:
                    text_instances = page.searchFor(personName, 30, False)
                    for inst in text_instances:
                        highlight = page.addHighlightAnnot(inst)
                        highlight.setColors({"stroke": (102 / 255, 224 / 255, 255 / 255)})
                        highlight.update()
            sentence_num += 1
        page_num += 1

    return data
