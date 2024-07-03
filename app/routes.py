from flask import render_template, flash, redirect, url_for, request  # Import necessary modules from flask (Hira Choudhry)
from app import app, db  # Import the app and db instances from the app module (Hira Choudhry)
from app.forms import LoginForm, RegistrationForm  # Import the LoginForm and RegistrationForm classes from app.forms (Hira Choudhry)
from app.models import User  # Import the User model from app.models (Hira Choudhry)
from flask_login import current_user, login_user, logout_user, login_required  # Import login-related functions from flask_login (Hira Choudhry)
from werkzeug.urls import url_parse  # Import url_parse from werkzeug.urls (Hira Choudhry)

# Define the base route (Hira Choudhry)
@app.route('/')
@app.route('/base')
@login_required  # Ensure the user is logged in to access this route (Hira Choudhry)
def base():
    return "Welcome to the Car Rental App!"  # Return a welcome message (Hira Choudhry)

# Define the login route (Hira Choudhry)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Check if the user is already authenticated (Hira Choudhry)
        return redirect(url_for('welcome'))  # Redirect to the welcome page if authenticated (Hira Choudhry)
    form = LoginForm()  # Create an instance of LoginForm (Hira Choudhry)
    if form.validate_on_submit():  # Check if the form is submitted and validated (Hira Choudhry)
        user = User.query.filter_by(username=form.username.data).first()  # Query the user by username (Hira Choudhry)
        if user is None:  # Check if the user does not exist (Hira Choudhry)
            print('User not found')  # Print debug message (Hira Choudhry)
            flash('Invalid username or password')  # Flash an error message (Hira Choudhry)
            return redirect(url_for('login'))  # Redirect to the login page (Hira Choudhry)
        if not user.check_password(form.password.data):  # Check if the password is incorrect (Hira Choudhry)
            print('Password does not match')  # Print debug message (Hira Choudhry)
            flash('Invalid username or password')  # Flash an error message (Hira Choudhry)
            return redirect(url_for('login'))  # Redirect to the login page (Hira Choudhry)
        login_user(user, remember=form.remember_me.data)  # Log in the user (Hira Choudhry)
        next_page = request.args.get('next')  # Get the next page from the request arguments (Hira Choudhry)
        if not next_page or url_parse(next_page).netloc != '':  # Check if the next page is valid (Hira Choudhry)
            next_page = url_for('welcome')  # Set the next page to the welcome page (Hira Choudhry)
        return redirect(next_page)  # Redirect to the next page (Hira Choudhry)
    return render_template('login.html', title='Sign In', form=form)  # Render the login template (Hira Choudhry)

# Define the signup route (Hira Choudhry)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:  # Check if the user is already authenticated (Hira Choudhry)
        return redirect(url_for('welcome'))  # Redirect to the welcome page if authenticated (Hira Choudhry)
    form = RegistrationForm()  # Create an instance of RegistrationForm (Hira Choudhry)
    if form.validate_on_submit():  # Check if the form is submitted and validated (Hira Choudhry)
        user = User.query.filter_by(username=form.username.data).first()  # Query the user by username (Hira Choudhry)
        if user is not None:  # Check if the username already exists (Hira Choudhry)
            flash('Please use a different username.')  # Flash an error message (Hira Choudhry)
            return redirect(url_for('signup'))  # Redirect to the signup page (Hira Choudhry)
        user = User.query.filter_by(email=form.email.data).first()  # Query the user by email (Hira Choudhry)
        if user is not None:  # Check if the email already exists (Hira Choudhry)
            flash('Please use a different email address.')  # Flash an error message (Hira Choudhry)
            return redirect(url_for('signup'))  # Redirect to the signup page (Hira Choudhry)
        new_user = User(  # Create a new user instance (Hira Choudhry)
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data
        )
        new_user.set_password(form.password.data)  # Set the user's password (Hira Choudhry)
        db.session.add(new_user)  # Add the new user to the database session (Hira Choudhry)
        db.session.commit()  # Commit the session to save the new user (Hira Choudhry)
        flash('Congratulations, you are now a registered user!')  # Flash a success message (Hira Choudhry)
        return redirect(url_for('login'))  # Redirect to the login page (Hira Choudhry)
    return render_template('signup.html', title='Register', form=form)  # Render the signup template (Hira Choudhry)

# Define the welcome route (Hira Choudhry)
@app.route('/welcome')
@login_required  # Ensure the user is logged in to access this route (Hira Choudhry)
def welcome():
    return render_template('welcome.html', title='Welcome')  # Render the welcome template (Hira Choudhry)

# Define the logout route (Hira Choudhry)
@app.route('/logout')
def logout():
    logout_user()  # Log out the user (Hira Choudhry)
    return redirect(url_for('login'))  # Redirect to the login page (Hira Choudhry)
