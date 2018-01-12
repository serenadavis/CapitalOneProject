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
    return render_template('Profile.html', username="test")

@app.route('/LendeeHome')
def Profile():
    return render_template('Profile.html')

@app.route('/RequestNewLoan')
def Profile():
    return render_template('RequestNewLoan.html')

@app.route('/ViewHistory')
def Profile():
    return render_template('ViewHistory.html')

@app.route('/ViewRequests')
def Profile():
    return render_template('ViewRequests.html')
