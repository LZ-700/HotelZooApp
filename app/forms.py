from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length, NumberRange, InputRequired
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Email not registered.')

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
    children = IntegerField('Children', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Book Tickets')
    def validate_visit_date(self, visit_date):
        if visit_date.data < date.today():
            raise ValidationError("Visit date cannot be in the past.")
    def validate(self):
        if not super().validate():
            return False
        if self.adults.data == 0 and self.children.data == 0:
            self.adults.errors.append("At least one adult or child must be included in the booking.")
            return False
        return True
    def validate_children(self, children):
        if self.adults.data == 0 and children.data > 0:
            raise ValidationError("Children cannot be booked without at least one adult.")

class HotelBookingForm(FlaskForm):
    check_in = DateField('Check-in Date', validators=[DataRequired()])
    check_out = DateField('Check-out Date', validators=[DataRequired()])
    num_guests = IntegerField('Number of Guests', validators=[DataRequired(), NumberRange(min=1)])
    special_requests = StringField('Special Requests')
    submit = SubmitField('Book Room')
    def validate_check_out(self, check_out):
        if self.check_in.data and check_out.data <= self.check_in.data:
              raise ValidationError("Check-out date must be after check-in date.")
