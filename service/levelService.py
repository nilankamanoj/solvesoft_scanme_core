from model import db
from model.level import Level
from service import partyService, levelSpecificSensitivityService, specificSensitivityService


def save_level(level):
    l = Level(level['name'], level['color'], level['scheme_id'], level['description'], level['is_party'], 0, [])
    db.session.add(l)
    db.session.commit()

    if l.is_party:
        include_level = get_level_by_name(level['include_level'])
        level['party'] = {'party_level_id': l.id, 'include_level_id': include_level.id}
        partyService.save_party_include_level(level['party'])
    for lss in level['level_specific_sensitivities']:
        lss['level_id'] = l.id
        levelSpecificSensitivityService.save_level_specific_sensitivity(lss)
    return l


def get_level_by_name(name):
    return Level.query.filter_by(name=name).first()


def get_levels_by_scheme_id(scheme_id):
    levels = Level.query.filter_by(scheme_id=scheme_id).all()
    for level in levels:
        if level.is_party:
            level.include_level_id = partyService.get_include_party_by_party_level_id(level.id).include_level_id

        lss = levelSpecificSensitivityService.get_level_specific_sensitivities_by_level_id(level.id)
        level.specific_sensitivities = [specificSensitivityService.get_specific_sensitivity(ls.specific_sensitivity_id)
                                        for ls in lss]
    return levels
