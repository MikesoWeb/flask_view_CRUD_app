import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite://memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(32)
    TEMPLATES_AUTO_RELOAD = False
    DEBUG = False
    TESTING = False


class ConfigDebug(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SERVER_NAME = 'localhost:5667'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///debug.db'


class ConfigProd(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
