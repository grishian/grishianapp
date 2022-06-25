from myapp import db
from myapp.bp_user import bp_user
from flask import render_template, flash, redirect, url_for, abort
from myapp.bp_user.form_user import UserForm
from myapp.bp_user.model_user import User


@bp_user.route('/user/<name>')
def do_user(name):
    return render_template('user.html', name=name)


@bp_user.route('/register', methods=['GET', 'POST'])
def do_register():
    return render_template('register.html')
