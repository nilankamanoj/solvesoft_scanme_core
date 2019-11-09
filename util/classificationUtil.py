import io
import pickle


class RenameUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        renamed_module = module
        if module == "StemmedCountVectorizer":
            renamed_module = "util.stemmedCountVectorizer"

        return super(RenameUnpickler, self).find_class(renamed_module, name)


def renamed_load(file_obj):
    return RenameUnpickler(file_obj, encoding='latin-1').load()


def renamed_loads(pickled_bytes):
    file_obj = io.BytesIO(pickled_bytes)
    return renamed_load(file_obj)


stream_classifier_p = open('util/classifiers/NB_stemmed.pickle', 'rb')
stream_classifier = renamed_load(stream_classifier_p)


def get_stream(txt):
    stream = stream_classifier.predict([txt])
    return stream[0].decode("utf-8")

