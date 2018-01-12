from app import db
from datetime import datetime, timedelta
import time, bcrypt

class Borrower(db.Model):
  id = db.Column(db.Integer , primary_key=True)
  email = db.Column(db.String(40), unique=True)
  first_name = db.Column(db.String())
  last_name = db.Column(db.String())
  pw_hash = db.Column(db.String())
  age = db.Column(db.Integer)
  location = db.Column(db.String())
  education = db.Column(db.String())
  facebook_url = db.Column(db.String())
  loans = db.relationship('Loan', backref='user', cascade="all, delete-orphan", lazy=True)

  def __init__(self, email, first_name, last_name, password):
    self.email = email
    self.first_name = first_name.lower()
    self.last_name = last_name.lower()
    self.pw_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

  def get_id(self):
    return str(self.id)

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'), self.pw_hash)

class Loan(db.Model):
  id = db.Column(db.Integer , primary_key=True)
  lend_date = db.Column(db.DateTime)
  paid_date = db.Column(db.DateTime)
  borrower_id = db.Column(db.Integer, db.ForeignKey('borrower.id'), nullable=False)
  principal = db.Column(db.Integer)
  interest_rate = db.Column(db.Integer)
  is_claimed = db.Column(db.Boolean)
  is_paid = db.Column(db.Boolean)
  is_spam = db.Column(db.Boolean)

  def __init__(self, lend_date, paid_date, borrower_id, lender_id, amount, interest_rate, is_claimed, is_paid, is_spam):
    self.lend_date = lend_date
    self.paid_date = paid_date
    self.borrower_id = borrower_id
    self.lender_id = lender_id
    self.principal = principal
    self.interest_rate = interest_rate
    self.is_claimed = is_claimed
    self.is_paid = is_paid
    self.is_spam = is_spam

  def get_id(self):
    return str(self.id)
