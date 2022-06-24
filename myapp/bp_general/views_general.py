from myapp.bp_general import bp_general
from flask import render_template, url_for, redirect, request, flash, abort


@bp_general.route('/')
def index():
    return render_template('index.html')
