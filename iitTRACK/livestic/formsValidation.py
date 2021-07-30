from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed, FileRequired 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField,FileField,HiddenField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class RegistrationForm(FlaskForm):
    	
	username=StringField('Username', validators=[DataRequired(), Length(min=3,max=15)])
	email=StringField('Email', validators=[DataRequired(), Email()])
    
	password=PasswordField('Password', validators=[DataRequired()])
	confirm_password=PasswordField('Confirm_Password', validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('sign up')

	def validate_username(self, username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken ,plz choose another one!')


	def validate_email(self, email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken ,plz choose another one!')




class LoginForm(FlaskForm):
	
	emails=StringField('Email', validators=[DataRequired(), Email()])
	password=PasswordField('Password', validators=[DataRequired()])
	remember=BooleanField('Remember me')
	submit=SubmitField('Login')

	def validate_email(self, email):
		email=User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('That email is taken ,plz choose another one!')
