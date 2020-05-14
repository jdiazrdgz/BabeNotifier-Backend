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
    PUSHER_APP_ID = '1001084'
    PUSHER_APP_KEY = '6ffe277684e3c8d0ef07'
    PUSHER_APP_SECRET = 'e83028229000f4ce0e2c'
    PUSHER_APP_CLUSTER = 'us2'
    PUSHER_APP_SSL = True
