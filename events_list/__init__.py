"""
This module initializes the Flask application, including configuration
settings, database setup, and import of routes and models.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
if os.path.exists(".env"):
    load_dotenv()

# Create Flask application instance
app = Flask(__name__)

# Application configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Ensure proper PostgreSQL URI format
if app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        app.config['SQLALCHEMY_DATABASE_URI'].replace(
            "postgres://", "postgresql://", 1)
    )

# Additional configuration
app.config['IP'] = os.getenv('IP', '127.0.0.1')
app.config['PORT'] = int(os.getenv('PORT', '5000'))

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes and models after initializing app
from events_list import routes, models  # noqa
