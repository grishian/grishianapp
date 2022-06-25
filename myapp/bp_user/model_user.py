import logging
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from myapp import db, login_manager
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    date_added = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Name %r>' % self.name

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
        # return user if user and (not user.is_banned or not user.is_active) else None
    except Exception as e:
        logging.error('error loading user {}: {}'.format(user_id, e))
    return None



