from app import db
from datetime import datetime, timedelta
import time

class Borrower(db.Model):
  id = db.Column(db.Integer , primary_key=True)
  email = db.Column(db.String(40), unique=True)
  first_name = db.Column(db.String())
  last_name = db.Column(db.String())
  age = db.Column(db.Integer)
  location = db.Column(db.String())
  education = db.Column(db.String())
  facebook_url = db.Column(db.String())
  loans = db.relationship('Loan', backref='user', lazy=True)

  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def get_id(self):
    return str(self.id)

class Loan(db.Model):
  id = db.Column(db.Integer , primary_key=True)
  lendDate = db.Column(db.DateTime)
  paidDate = db.Column(db.DateTime)
  borrower_id = db.Column(db.Integer, db.ForeignKey('borrower.id'), nullable=False)
  principal = db.Column(db.Integer)
  interest_rate = db.Column(db.Integer)
  is_claimed = db.Column(db.Boolean)
  is_paid = db.Column(db.Boolean)
  is_spam = db.Column(db.Boolean)

  def __init__(self, lendDate, paidDate, borrower_id, lender_id, amount, interest_rate, is_claimed, is_paid, is_spam):
    self.lendDate = lendDate
    self.paidDate = paidDate
    self.borrower_id = borrower_id
    self.lender_id = lender_id
    self.principal = principal
    self.interest_rate = interest_rate
    self.is_claimed = is_claimed
    self.is_paid = is_paid
    self.is_spam = is_spam

  def get_id(self):
    return str(self.id)
