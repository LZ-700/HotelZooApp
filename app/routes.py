from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm, RegistrationForm, ZooBookingForm, HotelBookingForm

bp = Blueprint('main', __name__) # App created later so that routes can be defined here without circular imports

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Invalid email or password")
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! You can now log in.")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@bp.route('/zoo-booking', methods=['GET', 'POST'])
@login_required
def zoo_booking():
    form = ZooBookingForm()
    if form.validate_on_submit():
        booking = ZooBooking(
        visit_date=form.visit_date.data,
        adults=form.adults.data,
        children=form.children.data,
        user_id=current_user.id
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('zoo_booking.html', form=form)

@bp.route('/hotel-booking', methods=['GET', 'POST'])
@login_required
def hotel_booking():
    form = HotelBookingForm()
    if form.validate_on_submit():
        booking = HotelBooking(
            check_in=form.check_in.data,
            check_out=form.check_out.data,
            room_type=form.room_type.data,
            user_id=current_user.id
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('hotel_booking.html', form=form)
