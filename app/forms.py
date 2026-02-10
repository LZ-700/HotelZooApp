class ZooBookingForm(FlaskForm):
    visit_date = DateField('Visit Date', validators=[DataRequired()])
    adults = IntegerField('Adults', validators=[DataRequired()])
    children = IntegerField('Children', validators=[DataRequired()])
    submit = SubmitField('Book Tickets')
