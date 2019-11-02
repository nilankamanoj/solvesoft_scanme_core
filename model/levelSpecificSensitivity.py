from model import db


class LevelSpecificSensitivity(db.Model):
    __tablename__ = 'level_specific_sensitivity'

    id = db.column(db.Integer(11), primary_key=True)
    level_id = db.column(db.ForeignKey(u'level.id', onupdate=u'CASCADE'))
    specific_sensitivity_id = db.column(db.ForeignKey(u'specific_sensitivity.id', onupdate=u'CASCADE'),
                                        index=True)
    created_time = db.column(db.Timestamp)

    level = db.relationship(u'Level')
    specific_sensitivity = db.relationship(u'SpecificSensitivity')