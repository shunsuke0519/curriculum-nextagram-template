import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or os.urandom(32)
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    S3_KEY = os.environ.get("S3_ACCESS_KEY")
    S3_SECRET =os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_LOCATION =os.environ.get("S3_DOMAIN")

class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False
    GOOGLE_CLIENT_ID=os.environ.get("GOOGLE_CLIENT_KEY")
    GOOGLE_CLIENT_SECRET=os.environ.get("GOOGLE_CLIENT_SECRET")



class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = False
    GOOGLE_CLIENT_ID=os.environ.get("GOOGLE_CLIENT_KEY")
    GOOGLE_CLIENT_SECRET=os.environ.get("GOOGLE_CLIENT_SECRET")


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True

