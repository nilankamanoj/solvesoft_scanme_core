from model.specificSensitivity import SpecificSensitivity


def get_specific_sensitivities_by_stream_id(stream_id):
    return SpecificSensitivity.query.filter_by(stream_id=stream_id).all()


def get_specific_sensitivity(id):
    return SpecificSensitivity.query.filter_by(id=id).first()
