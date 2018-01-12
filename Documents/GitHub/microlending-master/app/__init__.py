from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jsglue import JSGlue

app = Flask(__name__, static_folder='static')
app.config.from_object('config')
jsglue = JSGlue(app)

db = SQLAlchemy(app)

with app.app_context():
  db.create_all()

from app import application
