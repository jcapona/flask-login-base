import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    LOG_FILE = os.environ.get("LOG_PATH")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    PROD = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
        "prod": ProductionConfig,
        "dev": DevelopmentConfig,
        "test": TestingConfig
}

