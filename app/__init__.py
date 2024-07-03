from flask import Flask  # Import the Flask class from the flask module (Hira Choudhry)
from flask_sqlalchemy import SQLAlchemy  # Import the SQLAlchemy class from the flask_sqlalchemy module (Hira Choudhry)
from flask_migrate import Migrate  # Import the Migrate class from the flask_migrate module (Hira Choudhry)
from flask_login import LoginManager  # Import the LoginManager class from the flask_login module (Hira Choudhry)

app = Flask(__name__)  # Create an instance of the Flask class for our web app (Hira Choudhry)

# Configure the Flask app with a secret key for session management (Hira Choudhry)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configure the Flask app to use SQLite as the database (Hira Choudhry)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create an instance of SQLAlchemy to handle database operations (Hira Choudhry)
db = SQLAlchemy(app)

# Create an instance of Migrate to handle database migrations (Hira Choudhry)
migrate = Migrate(app, db)

# Create an instance of LoginManager to handle user session management (Hira Choudhry)
login = LoginManager(app)
login.login_view = 'login'  # Specify the view to redirect users to when they need to log in (Hira Choudhry)

# Import the routes and models modules (Hira Choudhry)
from app import routes, models  # Hira Choudhry
