from app import app, db
from .models import Borrower, Loan
from flask import Flask, redirect, url_for, session, request, jsonify, render_template

@app.route('/')
def index():
  return render_template('borrowers.html')

@app.route('/borrowers')
def borrowers():
  borrowers = Borrower.query.all()
  print("here are the borrowers: ", borrowers)
  return render_template('borrowers.html', borrowers=borrowers)

@app.route('/Profile')
def Profile():
    if current_user.is_authenticated:
        return render_template('Profile_Authenticated.html', name="test", score="8.4", age="50", edu="Undergraduate Degree", history="")
    else:
        return return render_template('Profile_Not_Authenticated.html', name="test", score="8.4", age="50", edu="Undergraduate Degree", history="")

@app.route('/LendeeHome')
def LendeeHome():
    return render_template('LendeeHome.html')

@app.route('/RequestNewLoan')
def RequestNewLoan():
    return render_template('RequestNewLoan.html')

@app.route('/ViewHistory')
def Profile():
    return render_template('ViewHistory.html')

@app.route('/ViewRequests')
def Profile():
    return render_template('ViewRequests.html')
