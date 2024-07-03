from app import db  # Import the db instance from the app module (Hira Choudhry)
from flask_login import UserMixin  # Import UserMixin class from flask_login module (Hira Choudhry)
from werkzeug.security import generate_password_hash, check_password_hash  # Import functions for password hashing and checking (Hira Choudhry)
from app import login  # Import the login instance from the app module (Hira Choudhry)

# Define the User class that inherits from UserMixin and db.Model (Hira Choudhry)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define the id column as the primary key (Hira Choudhry)
    username = db.Column(db.String(64), index=True, unique=True)  # Define the username column with indexing and uniqueness (Hira Choudhry)
    email = db.Column(db.String(120), index=True, unique=True)  # Define the email column with indexing and uniqueness (Hira Choudhry)
    first_name = db.Column(db.String(64))  # Define the first_name column (Hira Choudhry)
    last_name = db.Column(db.String(64))  # Define the last_name column (Hira Choudhry)
    phone = db.Column(db.String(15))  # Define the phone column (Hira Choudhry)
    password_hash = db.Column(db.String(128))  # Define the password_hash column (Hira Choudhry)

    # Define the set_password method to hash the password (Hira Choudhry)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Define the check_password method to verify the password (Hira Choudhry)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Define the __repr__ method to return a string representation of the user (Hira Choudhry)
    def __repr__(self):
        return '<User {}>'.format(self.username)

# Define the user_loader callback function for Flask-Login (Hira Choudhry)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))  # Load the user by ID (Hira Choudhry)
