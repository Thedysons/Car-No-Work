from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class SignUpForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=6,max=16)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Sign Up")

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=6,max=16)])
    submit = SubmitField(label="Login")

class ForgotPasswordForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    submit = SubmitField(label="Submit email")


class RequestHelpForm(FlaskForm):
    problem_description = StringField(label="Enter your problem")
    location = StringField(label="Enter your location")
    plate_number = StringField(label="Enter your plate number")
    car_model = StringField(label="Enter your car model")
    next = SubmitField(label="Next")

class PaymentOption(FlaskForm):
    payment_option = SelectField(u'Payment Type', choices=[('Member','Plan Membership'), ('OneOff','One Off Payment')])
    next = SubmitField(label="Next")

class MockCreditCardPayment(FlaskForm):
    name = StringField(label="Name On Card", validators=[DataRequired(), Length(min=3, max=20)])
    card_number = StringField(label="Card Number", validators=[DataRequired(), Length(min=3, max=20)])
    card_cv = StringField(label="Last 3 number on back of card", validators=[DataRequired(), Length(min=3, max=20)])
    expiary_date =StringField(label="Expiry date of card (mm/yyyy)", validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField(label="Make Payment")

class TakeJobForm(FlaskForm):
    accept_job = StringField(label="Accept Job (enter job number)")
    decline_job = StringField(label="Decline Job (ener job number)")
    submit = SubmitField(label="Submit Jobs to decline and/or accept")


class StartJobForm(FlaskForm):
    distance = StringField(label="How far are you from client (km)",  validators=[DataRequired()])
    location = StringField(label="Enter your location",  validators=[DataRequired()])
    time = StringField(label="Enter how long you are away",  validators=[DataRequired()])
    name = StringField(label="Enter your name",  validators=[DataRequired()])
    submit = SubmitField(label="Start Job")

class arrivedForm(FlaskForm):
    submit = SubmitField(label="Notify Client that you have arrived")

class finishJobForm(FlaskForm):
     submit = SubmitField(label="Click to finish job")

class completeJobForm(FlaskForm):
    report = TextAreaField(u'Report and final notes on job', validators =[Length(max=600)])
    submit = SubmitField(label="Click to confirm completion of job")