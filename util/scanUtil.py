import re

import nltk


def get_human_names(text):
    person_list = []
    tokens = nltk.tokenize.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos_tags, binary=False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1:
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
    return person_list


def get_telephone_numbers(text):
    telephone_list = []
    return telephone_list


def get_emails(text):
    rgx = r'[\w\.-]+@[\w\.-]+'
    print("test")
    email_list = re.findall(rgx, text)
    print(email_list)
    return email_list
