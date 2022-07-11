from myapp.bp_general import bp_general
from flask import render_template, url_for, redirect, request, flash, abort


@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    return render_template('general/home.html')
