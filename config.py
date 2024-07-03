import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # Secret key for CSRF protection (Hira Choudhry)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'  # SQLite database URI (Hira Choudhry)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking (Hira Choudhry)
