from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()


def create_app(config=None):
    app = Flask(__name__)

    app.debug = True

    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.session_protection = "basic"
    login_manager.login_view = 'do_login'

    do_register_blueprints(app)

    migrate.init_app(app, db)
    return app


def do_register_blueprints(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_user import bp_user

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_user)
