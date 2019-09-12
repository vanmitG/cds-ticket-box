from flask import Blueprint, render_template, redirect, url_for, request
from src import db
from src.components.events.forms import AddForm, DelForm
from src.components.users.forms import  NewUser
from src.models.users import Users

users_blueprint = Blueprint('users',
                             __name__,
                             template_folder='../../templates/users')



@users_blueprint.route('/add', methods=['GET', 'POST'])
def add_new_user():
  form = NewUser()
  if request.method== 'POST':
    if form.validate_on_submit():
      new_user = Users(name=form.name.data,
                        username = form.username.data)
      db.session.add(new_user)
      db.session.commit()
      return "KHOA IS OK"
  return render_template('register.html', form = form)
