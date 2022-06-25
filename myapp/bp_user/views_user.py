import logging
from myapp import db
from myapp.bp_user import bp_user
from flask import render_template, flash, redirect, url_for, abort, request
from flask_login import current_user, logout_user, login_user, login_required
from myapp.bp_user.model_user import User, only_admins


@bp_user.route('/user/<name>')
def do_user(name):
    return render_template('user/user.html', name=name)


@bp_user.route('/register', methods=['GET', 'POST'])
def do_register():
    if request.method == 'POST':
        username = request.form.get('input_username')
        password = request.form.get('input_password')
        password_check = request.form.get('input_password_check')

        if password_check == password:
            user = User()
            user.username = username
            user.set_password(password)
            user.active = True
            user.profile_type = 1

            db.session.add(user)
            db.session.commit()
            flash('Account created.', 'OK')
            return redirect(url_for('bp_user.do_login'))
        else:
            flash('Passwords do not match.', 'ERROR')

    return render_template('user/register.html')


@bp_user.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'POST':
        username = request.form.get('input_username')
        password = request.form.get('input_password')

        user = User.query.filter_by(username=username).first()
        if user:
            if not user.check_password(password):
                flash('That combination does not exist.', 'ERROR')
            else:
                # in case we have another user still logged in
                if current_user and current_user.is_authenticated:
                    try:
                        current_user.authenticated = False
                        db.session.add(current_user)
                        db.session.commit()
                        logout_user()
                    except Exception as e:  # pragma: no cover
                        # if this fails we do not care, but we certainly do not want to block
                        # someone logging in
                        logging.info('Error during login (logout): {}'.format(e))

                # now set the new user to authenticated
                user.authenticated = True
                db.session.add(user)
                db.session.commit()

                # do the actual login
                login_user(user)
                flash('Logged in.', 'OK')
                return redirect(url_for('bp_user.do_user', name=current_user.username))
        else:
            flash('Username does not exist.', 'ERROR')

    return render_template('user/login.html')


@bp_user.route("/logout", methods=["GET"])
@login_required
def do_logout():
    user = current_user
    if user and user.is_authenticated:
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        flash('You are now logged out', 'OK')
        logout_user()
        return redirect(url_for('bp_general.do_home'))


@bp_user.route('/user_list')
@only_admins
def do_user_list():
    users = User.query.all()
    return render_template('user/user_list.html', users=users)
