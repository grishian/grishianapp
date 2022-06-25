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
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(username=form.username.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.username.data
        form.username.data = ''
        form.email.data = ''
        flash('{} added successfully!'.format(name), 'OK')
    our_users = User.query.order_by(User.date_added)

    return render_template('register.html',
                           form=form,
                           our_users=our_users)
