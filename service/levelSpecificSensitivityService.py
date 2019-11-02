from model import db
from model.levelSpecificSensitivity import LevelSpecificSensitivity


def save_level_specific_sensitivity(level_specific_sensitivity):
    lss = LevelSpecificSensitivity(level_specific_sensitivity['level_id'],
                                   level_specific_sensitivity['specific_sensitivity_id'])
    db.session.add(lss)
    db.session.commit()
    return lss


def get_level_specific_sensitivities_by_level_id(level_id):
    return LevelSpecificSensitivity.query.filter_by(level_id=level_id).all()
