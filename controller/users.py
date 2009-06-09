# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

import re
from datetime import datetime

from controller.base import PublicPage
from controller.auth import login, signup

PRIVATE_HOME_URL = '/concurso'

class LoginPage(PublicPage):

    def post(self):
        try:
            username = self.request.get('username')
            password = self.request.get('password')
            assert username and password
            user = login(username, password)
            self.redirect(PRIVATE_HOME_URL)
        except Exception:
            self.render(self.template_name, {'login_error': True})

class RegisterPage(PublicPage):

    USERNAME_PATTERN = re.compile('[a-z][a-z0-9_]+')
    EMAIL_PATTERN = re.compile('^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$')

    def post(self):
        signup_args, errors = self.validate(*(self.request.get(i) for i in \
                ('username', 'password', 'confirm_password', 'mail', \
                'firstname', 'lastname', 'birthday', 'birthmonth', \
                'birthyear', 'dni', 'registration_reference', 'accept_tos')))
        if errors:
            self.render(self.template_name, errors)
        else:
            self.signup(*signup_args)
            self.redirect(PRIVATE_HOME_URL)

    def validate(username, password, confirm_password, mail, firstname, \
            lastname, birthday, birthmonth, birthyear, dni, \
            registration_reference, accept_tos):
        errors = {}
        if not (len(username) >= 4 and self.USERNAME_PATTERN.match(username)):
            errors['username'] = username
        if not (len(password) >= 8 and password == confirm_password):
            errors['password'] = ''
        if not self.EMAIL_PATTERN.match(mail):
            errors['mail'] = mail
        if not firstname.strip():
            errors['firstname'] = firstname
        if not lastname.strip():
            errors['lastname'] = lastname
        birthtuple = (birthyear, birthmonth, birthday)
        try:
            birthdate = datetime(int(i) for i in birthtuple)
        except Exception:
            errors['birthdate'] = '-'.join(birthtuple)
        try:
            dni = int(dni)
            assert dni >= 1000000 and dni < 100000000 # in [1M, 100M)
        except Exception:
            errors['dni'] = dni
        if not accept_tos:
            errors['accept_tos'] = False
        signup_args = (username, password, mail, firstname, lastname, \
                birthdate, dni, registration_reference)
        return (signup_args, errors)

