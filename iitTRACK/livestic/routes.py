from datetime import datetime
import os
import secrets

from flask import render_template, redirect, request, url_for, flash, current_app, abort, session, jsonify
from livestic import app, db
from livestic.formsValidation import RegistrationForm
from livestic.dataTables import User, Animals
from flask_login import login_user, current_user, logout_user, login_required
import json
from sqlalchemy import func
import smtplib, ssl

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/SignUp', methods=["POST", "GET"])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_pass=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user_1= User(name=form.username.data, email=form.email.data,  password=hashed_pass)
		db.session.add(user_1)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='register', form=form)


	
@app.route('/Login', methods=["POST", "GET"])
def login():
	return render_template('login.html')

	
