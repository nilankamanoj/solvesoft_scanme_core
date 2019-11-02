from os.path import dirname, realpath


class Configuration:
    UPLOAD_FOLDER = dirname(realpath(__file__)) + '/uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    SQLALCHEMY_DATABASE_URI = 'mysql://newuser2:password@localhost/fyp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'memcached'
    SECRET_KEY = 'super secret key'
    JWT_HEADER_NAME = 'authToken'
    JWT_SECRET_KEY = 'you will never guess me'
    JWT_ENCODING_ALGORITHM = 'HS256'
    JWT_LIFETIME = 3600 * 24 * 7
