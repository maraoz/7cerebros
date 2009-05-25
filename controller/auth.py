# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

import logging
import md5

from google.appengine.ext import webapp, db

from model.persistence.datamodels import User
from model.persistence.sessions import Session

logger = logging.getLogger(__name__)

class AuthenticationError(Exception):
    """ Raised when authentication fails (invalid credentials) """

class PermissionError(Exception):
    """ Raised when authenticated user has no rights to do an operation """

def authorize(admin=False, user_arg='user', session_arg='session'):
    """
    Decorator factory to authorize a user to perform a restricted operation.
    If `admin` flag is set, also checks is user has admin rights.
    Example: Use @autorize(...) on a request handler method.

    :parameters:
        admin : bool
            Optional flag to check admin rights (default: `False`)
        key : str
            Keyword argument to be appended to decorated function

    :returns:
        Decorator function to be applied on a restricted operation.
    """
    def authorize_decorator_wrap(decorated_function):
        def authorize_decorator(*args, **kwargs):
            session = Session()
            user = authenticate(session)
            if admin and not is_admin(user):
                raise PermissionError
            if user_arg is not None:
                kwargs[user_arg] = user
            if session_arg is not None:
                kwargs[session_arg] = session
            return decorated_function(*args, **kwargs)
        return authorize_decorator
    return authorize_decorator_wrap

def authenticate(session):
    """
    Returns a user if authentication succeeds, or else raises an exception.

    :parameters:
        session : `Session`
            Session object (that identifies user with session['username'])

    :returns:
        `User` instance corresponding to the authenticated user.

    :raises:
        `AuthenticationError` if authentication fails.
    """
    user = None
    try:
        username = session.get('username')
        if username is not None:
            user = db.query(User).filter('username', username).get()
    except Exception:
        logger.exception('Failed to authenticate user')
    if user is None:
        raise AuthenticationError
    return user

def is_admin(user):
    """ Returns `True` only if the user has admin rights """
    return user.username in ['admin', 'scoffey'] # TODO

def signup(username, password, confirm_password, mail, firstname, \
        lastname, birthdate, dni, registration_reference):
    USERNAME_PATTERN = re.compile('[a-z][a-z0-9_]+')
    EMAIL_PATTERN = re.compile('^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$')
    # TODO
    errors = {}
    if not (len(username) >= 4 and USERNAME_PATTERN.match(username)):
        errors['username'] = username
    if not (len(password) >= 8 and password == confirm_password):
        errors['password'] = ''
    user = User(username=username, password=secretize(password), mail=mail, \
        firstname=fistname, lastname=lastname, birthdate=birthdate, dni=dni, \
        registration_reference=registration_reference)
    user.put()
    session = Session()
    session['username'] = username
    return user

def login(username, password):
    """
    Initializes session data for authentication if credentials are valid.
    Otherwise, raises an exception.

    :parameters:
        username : str
            User name (ID)
        password : str
            User password

    :raises:
        `AuthenticationError` if the given credentials are not valid.

    :returns:
        `User` instance corresponding to the user that logged in.
    """
    user = None
    try:
        user = db.query(User).filter('username', username). \
                filter('password', secretize(password)).get()
    except Exception:
        logger.exception('Failed to log user in')
    if user is None:
        # TODO: retry with legacy UserStore model
        raise AuthenticationError
    session = Session()
    session['username'] = username
    return user

def logout():
    """ Clears the session data """
    session = Session()
    session.clear()

def secretize(password):
    """ Returns a hashed version of the given password, as to be saved """
    # DO NOT CHANGE THIS SECRET SALT UNLESS YOU KNOW WHAT YOU ARE DOING
    SECRET_SALT = 'w4Lt3r RuLeZ!'
    hash = md5.new(password)
    hash.update(SECRET_SALT)
    return hash.hexdigest()

