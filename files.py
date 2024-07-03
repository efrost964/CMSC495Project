import os

directories = [
    "app",
    "app/templates"
]

files = [
    "app/__init__.py",
    "app/models.py",
    "app/forms.py",
    "app/routes.py",
    "app/templates/base.html",
    "app/templates/login.html",
    "app/templates/signup.html",
    "config.py",
    "run.py",
    "db.sqlite"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

for file in files:
    with open(file, 'w') as f:
        pass

print("Project structure created successfully.")
