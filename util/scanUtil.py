import re

import nltk


def get_human_names(text):
    person_list = []
    tokens = nltk.tokenize.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos_tags, binary=False)

    person = []
    person2 = []
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
        elif len(person) > 0:
            person2.append(person[0])

        person = []

    i = 0
    while len(person2) > i:
        if len(person2) - 1 == i:
            person_list.append(person2[i])
            break
        else:
            person = re.findall("[\s]" + person2[i] + "[\s]+" + person2[i + 1] + "[\s]", text)
            if len(person) > 0:
                person_list.append(person[0][1:-1])
                i += 2
            else:
                person = re.findall("^" + person2[i] + "[\s]+" + person2[i + 1] + "[\s]", text)
                if len(person) > 0:
                    person_list.append(person[0][0:-1])
                    i += 2
                else:
                    person_list.append(person2[i])
                    i += 1
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
