from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length, NumberRange
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=21)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered.')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken.')

class ZooBookingForm(FlaskForm):
    visit_date = DateField('Visit Date', validators=[DataRequired()])
    adults = IntegerField('Adults', validators=[DataRequired(), NumberRange(min=0)])
    children = IntegerField('Children', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Book Tickets')

class HotelBookingForm(FlaskForm):
    check_in = DateField('Check-in Date', validators=[DataRequired()])
    check_out = DateField('Check-out Date', validators=[DataRequired()])
    room_type = SelectField('Room Type', choices=[
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite')
    ], validators=[DataRequired()])
    submit = SubmitField('Book Room')
    def validate_check_out(self, check_out):
        if self.check_in.data and check_out.data <= self.check_in.data:
              raise ValidationError("Check-out date must be after check-in date.")
