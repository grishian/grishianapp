class BaseConfiguration():
    DEBUG = True
    SECRET_KEY = 'my secret key'

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://ppcgnjbgfpjuzr:d74db855ab3944cd27385f1c94fe43c164582840632c02f78deceb9650f8bb3c@ec2-3-226-163-72.compute-1.amazonaws.com:5432/d82t048gtm2ur9'
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
