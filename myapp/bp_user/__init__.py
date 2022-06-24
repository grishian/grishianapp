from flask import Blueprint

bp_user = Blueprint('bp_user', __name__, cli_group="user")

from . import views_user