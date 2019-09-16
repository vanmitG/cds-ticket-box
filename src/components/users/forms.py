from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from src.models.users import Users


class AddForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired('Please enter your first name'), Length(
        min=3, max=100, message="at least 3 chars and at most 100 chars")])
    last_name = StringField('Last name', validators=[DataRequired('Please enter your last name'), Length(
        min=3, max=100, message="at least 3 chars and atmost 100 chars")])
    username = StringField('Username', validators=[DataRequired('Please enter your username'), Length(
        min=3, max=100, message="at least 3 chars and at most 100 chars")])
    email = StringField('Email', validators=[DataRequired(
        'Please enter your email address'), Email('Please input a valid email')])
    password = PasswordField('Password', validators=[DataRequired(
        'Please enter your password'), Length(
        min=3, max=128, message="at least 3 chars and at most 128 chars"), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Confirm Password')
    # TODO validate image link
    image_url = StringField('Your beautiful image link')

    submit = SubmitField('Add User')

    def validate_username(self, field):
        if Users.query.filter_by(user_name=field.data).first():
            raise ValidationError('Your username has been registered')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered')


class Login(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired('Please enter your email address'), ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Event to Remove:')
    submit = SubmitField('Remove Event')
