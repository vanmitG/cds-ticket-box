from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from src import db
from src.components.users.forms import AddForm, DelForm, Login
from src.models.users import Users

users_blueprint = Blueprint('user',
                            __name__,
                            template_folder='../../templates')


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out, lets come back', 'info')
    return redirect(url_for('user.login'))


@users_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    form = Login()
    if request.method == 'POST':
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('user.list'))
            else:
                flash(['your password is incorrect'])
                return redirect(url_for('user.login'))

        else:
            flash(["email address not exist"])
            return redirect(url_for('user.add'))
    return render_template('users/login.html', form=form)


@users_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            u = Users(img_url=form.image_url.data, last_name=form.last_name.data,
                      first_name=form.first_name.data, user_name=form.username.data, email=form.email.data)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            # login_user(u)
            flash(
                f'Successfuly sign up {u.email}. Please Login!!!', 'success')
            return redirect(url_for('user.list'))
        else:
            print(form.errors)
            for field_name, errors in form.errors.items():
                flash(errors)
    return render_template('users/add.html', form=form)


@users_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    users = Users.query.all()
    return render_template('users/list.html', users=users)


@users_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Users.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('user.list'))
    return render_template('users/delete.html', form=form)


@users_blueprint.route('/schema', methods=['GET'])
def schema():
    return render_template('users/schema.html')
