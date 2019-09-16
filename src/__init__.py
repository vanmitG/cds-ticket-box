import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

POSTGRES = {
    'user': os.environ['PSQL_USER'],
    'pw': os.environ['PSQL_PWD'],
    'db': os.environ['PSQL_DB'],
    'host': os.environ['PSQL_HOST'],
    'port': os.environ['PSQL_PORT'],
}

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = os.environ['MY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
admin_mgr = Admin(app, template_mode='bootstrap3')

login_mgr = LoginManager(app)
login_mgr.login_view = 'users.login'
login_mgr.init_app(app)

from src.models.users import Users  # noqa
from src.models.event import Events  # noqa
admin_mgr.add_view(ModelView(Users, db.session))
admin_mgr.add_view(ModelView(Events, db.session))


@login_mgr.user_loader
def load_user(id):
    return Users.query.get(int(id))


# the line noqa is prevent from statement to be moved up
from src.components.users.views import users_blueprint  # noqa

from src.components.c_events.views import events_blueprint  # noqa

app.register_blueprint(events_blueprint, url_prefix='/events')
app.register_blueprint(users_blueprint, url_prefix='/users')
