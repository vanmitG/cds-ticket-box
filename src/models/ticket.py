# from src.models import db
# from datetime import datetime

# # this class can be more detail and splited into two class for larger project


# class Tickets(db.Model):

#     __tablename__ = 'tickets'

#     id = db.Column(db.Integer, primary_key=True)
#     typeName = db.Column(db.String(40), nullable=False)
#     price = db.Column(db.Integer, default=0)
#     max_quantity = db.Column(db.Integer, default=10)
#     seat_id = db.Column(db.Integer, default=1)
#     event_id = db.Column(db.Integer, db.ForeignKey(
#         'events.id'), nullable=False)

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     def __repr__(self):
#         return f"{self.id} ticket is of type{self.typeName} of {self.event_id}."
