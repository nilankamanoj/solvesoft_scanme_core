from passlib.hash import pbkdf2_sha256 as sha256

from model import db


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.Integer)
    is_enabled = db.Column(db.Boolean)

    def __init__(self, name, email, password, role, is_enabled):
        self.name = name
        self.email = email
        self.password = User.generate_hash(password)
        self.role = role
        self.is_enabled = is_enabled

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'is_enabled': self.is_enabled,
            'role': self.role,
        }

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
