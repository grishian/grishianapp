from myapp.bp_user import bp_user
from flask import render_template, flash, redirect, url_for, abort
from myapp.bp_user.form_user import UserForm


@bp_user.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@bp_user.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash('User added successfully!', 'OK')
    our_users = Users.query.order_by(Users.date_added)

    return render_template('add_user.html',
                           form=form,
                           name=name,
                           our_users=our_users)
