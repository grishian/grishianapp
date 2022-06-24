class BaseConfiguration():
    DEBUG = True
    SECRET_KEY = 'my secret key'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'

    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
