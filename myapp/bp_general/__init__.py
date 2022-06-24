from flask import Blueprint

bp_general = Blueprint('bp_general', __name__, cli_group="db")

from . import views_general
