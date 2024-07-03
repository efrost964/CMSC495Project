from flask_wtf import FlaskForm  # Import FlaskForm from flask_wtf (Hira Choudhry)
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # Import form fields from wtforms (Hira Choudhry)
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Regexp  # Import validators from wtforms (Hira Choudhry)
from email_validator import validate_email, EmailNotValidError  # Import email validation functions (Hira Choudhry)
from app.models import User  # Import the User model from the app.models module (Hira Choudhry)

# Define the LoginForm class that inherits from FlaskForm (Hira Choudhry)
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # Define the username field with DataRequired validator (Hira Choudhry)
    password = PasswordField('Password', validators=[DataRequired()])  # Define the password field with DataRequired validator (Hira Choudhry)
    remember_me = BooleanField('Remember Me')  # Define the remember_me checkbox (Hira Choudhry)
    submit = SubmitField('Login')  # Define the submit button (Hira Choudhry)

# Define the RegistrationForm class that inherits from FlaskForm (Hira Choudhry)
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])  # Define the first_name field with DataRequired validator (Hira Choudhry)
    last_name = StringField('Last Name', validators=[DataRequired()])  # Define the last_name field with DataRequired validator (Hira Choudhry)
    username = StringField('Username', validators=[DataRequired()])  # Define the username field with DataRequired validator (Hira Choudhry)
    email = StringField('Email', validators=[DataRequired(), Email()])  # Define the email field with DataRequired and Email validators (Hira Choudhry)
    phone = StringField('Phone Number', validators=[
        DataRequired(), 
        Regexp(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    ])  # Define the phone field with DataRequired and Regexp validators (Hira Choudhry)
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Regexp(r'(?=.*\d)', message="Password must contain a number."),
        Regexp(r'(?=.*[A-Z])', message="Password must contain an uppercase letter."),
        Regexp(r'(?=.*[a-z])', message="Password must contain a lowercase letter."),
        Regexp(r'(?=.*[\W_])', message="Password must contain a symbol.")
    ])  # Define the password field with multiple validators (Hira Choudhry)
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])  # Define the confirm_password field with DataRequired and EqualTo validators (Hira Choudhry)
    submit = SubmitField('Sign Up')  # Define the submit button (Hira Choudhry)

    # Define a custom validator for the username field (Hira Choudhry)
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # Define a custom validator for the email field (Hira Choudhry)
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    # Define a custom validator for the password field (Hira Choudhry)
    def validate_password(self, password):
        common_passwords = ['password', '12345678', 'qwerty', 'abc123', 'letmein', 'password1']
        if password.data in common_passwords:
            raise ValidationError('Please choose a more secure password.')
