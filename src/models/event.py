from src import db
from datetime import datetime


class Events(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
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
    tickets = db.relationship('Ticket', backref='events', lazy="dynamic")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} event_name is {self.name}."


class Tickets(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    typeName = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, default=0)
    max_quantity = db.Column(db.Integer, default=10)
    seat_id = db.Column(db.Integer, default=1)
    event_id = db.Column(db.Integer, db.ForeignKey(
        'events.id'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} ticket is of type{self.typeName} of {self.event_id}."
