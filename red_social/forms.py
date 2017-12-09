"""Py-Social-Network"""
"""Autor: Luis Gerardo Aguayo Lopez y Carla del Carmen Barcenas Castillo"""
"""GITI9072"""
"""Red social se basa en un reto llevar acabo una red social la cual vamos a poder registrar, iniciar sesion, 
publicar y ver publicaciones de otros usuarios ."""
from flask_wtf import Form

#Flask-WTF uses wtforms behind the scenes for the actual form, field, and widget creation.
from wtforms import PasswordField
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import ValidationError

from models import User

def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError('User with this name already exists.')

def email_exists(form,field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('User with this email already exists.')

class RegisterForm(Form):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Regexp(
				r'^[a-zA-Z0-9_]+$',
				message = ("Username should be one word, letters, numbers and underscores only.")
				),
			name_exists
		])

	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			email_exists
		])

	password = PasswordField(
		'Password',
		validators=[
			DataRequired(),
			Length(min=6),
			EqualTo('password2', message = 'Passwords must match')
		])
	password2 = PasswordField(
		'Confirm Password',
		validators=[DataRequired()
		])


class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])

class PostForm(Form):
	content = TextAreaField("What's Up?", validators = [DataRequired()])