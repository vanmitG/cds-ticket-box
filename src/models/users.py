from flask_login import UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from src import db


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(80), default="User")
    password_hash = db.Column(db.String(128), nullable=False)
    img_url = db.Column(
        db.String(128), default="https://randomuser.me/api/portraits/men/77.jpg")
    events = db.relationship("Events", backref="users", lazy="dynamic")
    # comments = db.relationship("Comments", backref="users", lazy="dynamic")
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(
        db.DateTime,  nullable=False, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} user_name is {self.user_name}."
