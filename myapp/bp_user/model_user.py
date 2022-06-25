import logging
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from myapp import db, login_manager
from datetime import datetime
from flask import abort


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    __password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    profile_type = db.Column(db.Integer, default=1)
    date_added = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Name %r>' % self.name

    def is_active(self):
        return self.active

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.__password, password)


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
        # return user if user and (not user.is_banned or not user.is_active) else None
    except Exception as e:
        logging.error('error loading user {}: {}'.format(user_id, e))
    return None


def only_admins(func):
    @wraps(func)
    def is_allowed(*args, **kwargs):
        cu = current_user
        if cu is not None and cu.profile_type == 0:
            return func(*args, **kwargs)
        else:
            abort(403)

    return is_allowed
