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
    ('/', bind(PublicPage, 'public/home.html')),
    ('/login', bind(PublicPage, 'public/home.html')),
    ('/sponsors', bind(PublicPage, 'public/sponsors.html')),
    ('/contacto', bind(PublicPage, 'public/contacto.html')),
    ('/info', bind(PublicPage, 'public/info.html')),
    ('/perfil', bind(PrivatePage, 'private/perfil.html')),
    ('/practica', bind(PrivatePage, 'practica/index.html')),
    ('/concurso', bind(PrivatePage, 'concurso/index.html')),
]

