# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp.util import run_wsgi_app

from controller.routes import ROUTES

def main():
    """ Web application main controller """
    application = WSGIApplication(ROUTES, debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()

