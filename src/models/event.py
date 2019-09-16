from src import db
from datetime import datetime


class Events(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # owner_id = db.relationship('User',backref='event', nullable=False)
    # owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, default=0)
    address = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration_start = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    duration_end = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    organizer_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    # tickets = db.relationship('Ticket', backref='events', lazy="dynamic")
    # owner_id = db.relationship('User',backref='event', nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} event_name is {self.name}."
