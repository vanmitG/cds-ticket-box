import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager, current_user
from flask_migrate import Migrate

app = Flask(__name__)

# POSTGRES = {
#     'user': os.environ['PSQL_USER'],
#     'pw': os.environ['PSQL_PWD'],
#     'db': os.environ['PSQL_DB'],
#     'host': os.environ['PSQL_HOST'],
#     'port': os.environ['PSQL_PORT'],
# }

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = os.environ['MY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# 'postgresql://%(user)s:%(pw)s@%(host)s:\
# %(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)
Migrate(app, db)
admin_mgr = Admin(app, template_mode='bootstrap3')

login_mgr = LoginManager(app)
login_mgr.login_view = 'user.login'
login_mgr.init_app(app)


from src.models.admin import AuthModelView  # noqa
from src.models.users import Users  # noqa
from src.models.event import Events  # noqa
admin_mgr.add_view(AuthModelView(Users, db.session))
admin_mgr.add_view(AuthModelView(Events, db.session))


@login_mgr.user_loader
def load_user(id):
    return Users.query.get(int(id))


# the line noqa is prevent from statement to be moved up
from src.components.users.views import users_blueprint  # noqa

from src.components.c_events.views import events_blueprint  # noqa

app.register_blueprint(events_blueprint, url_prefix='/events')
app.register_blueprint(users_blueprint, url_prefix='/users')
