import os

import fitz

from config import Configuration
from model.documentRelease import DocumentRelease
from model.violation import Violation
from service.levelService import get_level_by_name
from service.releaseService import save_release
from service.violationService import create_violation
from util.asposeUtil import get_replacer, replace_file
from service.fileService import get_document_by_name


def highlight_pdf(data, scheme):
    colors = re_arrange_scheme(scheme)
    doc = fitz.open(Configuration.UPLOAD_FOLDER + "/" + data['baseFileName'] + ".pdf")
    page_num = 0
    page_data = data['data']
    for page in doc:
        sentences = page_data[page_num]['sentences']
        for sentence in sentences:
            if sentence['checked'] and len(sentence['spec']) > 1 and colors[sentence['spec']] is not None:
                highlight_phrase(sentence['text'], page, colors[sentence['spec']])
            else:
                for name in sentence['names']:
                    if name['checked']:
                        highlight_phrase(name['data'], page, '23,150,46')
                for email in sentence['emails']:
                    if email['checked']:
                        highlight_phrase(email['data'], page, '204, 51, 255')

        for email in page_data[page_num]['emails']:
            if email['checked']:
                highlight_phrase(email['data'], page, '204, 51, 255')
        page_num += 1
    doc.save(os.path.join(Configuration.UPLOAD_FOLDER, data['baseFileName'] + str(data['version']) + '.pdf'))


def highlight_phrase(phrase, page, color):
    rgb = list(map(int, color.split(',')))
    text_instances = page.searchFor(phrase, 200, False)
    for inst in text_instances:
        highlight = page.addHighlightAnnot(inst)
        highlight.setColors({"stroke": (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)})
        highlight.update()


def re_arrange_scheme(scheme):
    spec_sensitivities = {}
    for level in scheme.levels:
        for ss in level.specific_sensitivities:
            spec_sensitivities[ss.name] = level.color
    return spec_sensitivities


def replace(data):
    exp_names = 0
    exp_email = 0

    replaces = []
    doc = fitz.open(Configuration.UPLOAD_FOLDER + "/" + data['baseFileName'] + ".pdf")
    page_num = 0
    page_data = data['data']
    for page in doc:
        sentences = page_data[page_num]['sentences']
        for sentence in sentences:
            if sentence['checked'] and len(sentence['spec']) > 1:
                # sentence replace
                continue
            else:
                for name in sentence['names']:
                    if name['checked']:
                        replaces.append(get_replacer(name['data'], '<person>'))
                    else:
                        exp_names += 1
                for email in sentence['emails']:
                    if email['checked']:
                        replaces.append(get_replacer(email['data'], '<person@email.t>'))
                    else:
                        exp_email += 1

        for email in page_data[page_num]['emails']:
            if email['checked']:
                replaces.append(get_replacer(email['data'], '<person@email.t>'))
            else:
                exp_email += 1
        page_num += 1
    level = get_level_by_name(data['release_level'])
    doc = get_document_by_name(data['name'])
    dr = DocumentRelease(level.id, doc.id)
    dr = save_release(dr)
    if exp_names > 0:
        v = Violation(release_id=dr.id, description=str(exp_names) + " names were exposed.", checked=False)
        create_violation(v)
    if exp_email > 0:
        v = Violation(release_id=dr.id, description=str(exp_email) + " emails were exposed.", checked=False)
        create_violation(v)

    return replace_file(replaces, data['baseFileName'])
