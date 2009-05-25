# -*- coding: utf-8 -*-
__docformat__='restructuredtext'

__all__ = ['ROUTES']

from controller.base import PublicPage, PrivatePage, AdminPage

def bind(controller_class, *args, **kwargs):
    """ Utility function to bind arguments to controller classes """
    class Page(controller_class):
        def __init__(self):
            super(Page, self).__init__(*args, **kwargs)
    return Page

# Map all URLs to their controllers here

ROUTES = [
    ('/', bind(PublicPage, 'common/index.mako')),
    ('/login', bind(PublicPage, 'common/login.mako')),
    ('/concurso/tetravex', bind(PrivatePage, 'concurso/tetravex.mako')),
    ('/concurso/sokoban', bind(AdminPage, 'concurso/sokoban.mako')),
]

