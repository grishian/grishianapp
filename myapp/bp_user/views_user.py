from myapp import db
from myapp.bp_user import bp_user
from flask import render_template, flash, redirect, url_for, abort, request
from myapp.bp_user.form_user import UserForm
from myapp.bp_user.model_user import User


@bp_user.route('/user/<name>')
def do_user(name):
    return render_template('user/user.html', name=name)


@bp_user.route('/register', methods=['GET', 'POST'])
def do_register():
    if request.method == 'POST':
        username = request.form.get('input_username')
        password = request.form.get('input_password')
        # password_check = request.form.get('input_password_check')

        user = User()
        user.username = username
        user.set_password(password)
        user.active = True
        user.profile_type = 1

        db.session.add(user)
        db.session.commit()

    return render_template('user/register.html')


@bp_user.route('/user_list')
def do_user_list():
    users = User.query.all()
    return render_template('user/user_list.html', users=users)
