# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

__all__ = ['ROUTES']

from controller.common import PublicPage, PrivatePage, AdminPage

def route(controller_class, *args, **kwargs):
    """ Utility function to bind arguments to controller classes """
    class Page(controller_class):
        def __init__(self):
            super(Page, self).__init__(*args, **kwargs)
    return Page

# Map all URLs to their controllers here

ROUTES = [
    ('/', route(PublicPage, 'common/index.mako')),
    ('/login', route(PublicPage, 'common/login.mako')),
    ('/concurso/tetravex', route(PrivatePage, 'concurso/tetravex.mako')),
    ('/concurso/sokoban', route(AdminPage, 'concurso/sokoban.mako')),
]

