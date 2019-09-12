from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, ValidationError


class NewUser(FlaskForm):
  name = StringField("Your name", validators=[DataRequired()])
  username = StringField("Your username", validators=[DataRequired()])
  submit = SubmitField("Submit")