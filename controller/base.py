# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

import os
import logging

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template

from controller.auth import authorize, AuthenticationError

logger = logging.getLogger(__name__)

class BaseController(webapp.RequestHandler):

    BASEDIR = os.path.join(os.path.dirname(__file__), os.pardir, 'view')

    def render(self, template_name, template_values=None):
        try:
            path = os.path.join(self.BASEDIR, template_name)
            output = template.render(path, template_values or {})
            self.response.out.write(output)
            return output
        except Exception:
            logger.exception('Failed to render template: %s %s', \
                    template_name, template_values)
            raise

    def handle_exception(self, exception, debug_mode):
        logger.error(exception)
        if isinstance(exception, AuthenticationError): # TODO: require login...
            self.render('common/notfound.html') # a forbidden error page
        self.render('common/error.html') # a server error page
        # TODO: set HTTP status: 500, 400, etc.
        # TODO: be verbose on debug_mode

class PublicPage(BaseController):

    def __init__(self, template_name):
        super(PublicPage, self).__init__()
        self.template_name = template_name

    def get(self):
        template_values = self.get_template_values()
        self.render(self.template_name, template_values)

    def get_template_values(self, **kwargs):
        return kwargs

class PrivatePage(PublicPage):

    @authorize()
    def get(self, user, session):
        template_values = self.get_template_values(user=user, session=session)
        self.render(self.template_name, template_values)

class AdminPage(PublicPage):

    @authorize(admin=True)
    def get(self, user, session):
        template_values = self.get_template_values(user=user, session=session)
        self.render(self.template_name, template_values)

