from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

if os.path.exists(".env"):
    load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['IP'] = os.getenv('IP', '127.0.0.1')
app.config['PORT'] = int(os.getenv('PORT', 5000))
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from events_list import routes 