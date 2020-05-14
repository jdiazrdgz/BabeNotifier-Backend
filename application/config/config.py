from unipath import Path


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    ENV = 'production'
    SESSION_COOKIE_SECURE = False
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = 'development'
    SESSION_COOKIE_SECURE = False
    PROPAGATE_EXCEPTIONS = True
