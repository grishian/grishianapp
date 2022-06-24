from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)

    app.debug = True

    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    do_register_blueprints(app)

    return app


def do_register_blueprints(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_user import bp_user

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_user)
