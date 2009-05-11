# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

# datamodels.py
# Model classes to be mapped in the database

from google.appengine.ext import db

class User(db.Model):
	username = db.StringProperty(required=True)
	password = db.StringProperty(required=True)
	mail = db.StringProperty()
	firstname = db.StringProperty()
	lastname = db.StringProperty()
	birthdate = db.DateTimeProperty()
	dni = db.IntegerProperty()
	registration_date = db.DateTimeProperty(auto_now_add=True)
	registration_reference = db.TextProperty()
	avatar = db.BlobProperty()

class Challenge(db.Model):
    name = db.StringProperty(required=True)
    group = db.StringProperty()
    start_date = db.DateTimeProperty()
    end_date = db.DateTimeProperty()

class ChallengeUserEvent(db.Model):
    challenge = db.ReferenceProperty(Challenge, required=True)
    user = db.ReferenceProperty(User, required=True)
    event = db.StringProperty(required=True, \
            choices=set(['start', 'end']))
    date = db.DateTimeProperty(auto_now=True)
    extra_data = db.TextProperty()

# ----- DEPRECATED LEGACY DATAMODELS -----

class UserStore(db.Model):

	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)

	mail = db.StringProperty()

	nombre = db.StringProperty()
	apellido = db.StringProperty()

	fuente = db.StringProperty(multiline=True)

	fecha_nac = db.DateTimeProperty()
	documento = db.IntegerProperty()
	#ciudad = db.StringProperty()

	registration_date = db.DateTimeProperty(auto_now_add=True)

	avatar = db.BlobProperty()


	problem_1_solve = db.DateTimeProperty()		# tetravex
	problem_2_solve = db.DateTimeProperty()		# max
	problem_3_solve = db.DateTimeProperty()		# sokoban
	problem_4_solve = db.DateTimeProperty()		# series
	problem_5_solve = db.DateTimeProperty()		# impossible
	problem_6_solve = db.DateTimeProperty()		# mensaje
	problem_7_solve = db.DateTimeProperty()		# automatas

	practice_1 = db.DateTimeProperty()		# coloreo
	practice_2 = db.DateTimeProperty()		# subset
	practice_3 = db.DateTimeProperty()		# walter
	practice_4 = db.DateTimeProperty()		# simplex
	practice_5 = db.DateTimeProperty()		# codigo secreto

	score = db.IntegerProperty()
	suma_de_tiempos = db.IntegerProperty()

class TicketStore(db.Model):

	nombre = db.StringProperty(required = True)
	apellido = db.StringProperty(required = True)
	mail = db.StringProperty(required = True)
	fuente = db.StringProperty(multiline=True)
	registration_date = db.DateTimeProperty(auto_now_add=True)

class UnsentEmail(db.Model):

	nombre = db.StringProperty(required = True)
	apellido = db.StringProperty(required = True)
	mail = db.StringProperty(required = True)
	fuente = db.StringProperty(multiline=True)


class UserCounter(db.Model):

	cantidad = db.IntegerProperty()

class LastPlayer(db.Model):
	username = db.StringProperty()
