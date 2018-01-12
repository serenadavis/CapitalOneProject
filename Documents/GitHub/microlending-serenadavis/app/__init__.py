from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jsglue import JSGlue
from flask_login import LoginManager

login_manager = LoginManager()


app = Flask(__name__, static_folder='static')
app.config.from_object('config')
jsglue = JSGlue(app)

db = SQLAlchemy(app)

from app.models import Borrower

@login_manager.user_loader
def load_user(id):
    return Borrower.query.get(id)

login_manager.init_app(app)

with app.app_context():
  db.create_all()

from app import application
