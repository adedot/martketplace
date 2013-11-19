from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.view import static

from pyramid.session import UnencryptedCookieSessionFactoryConfig

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    # Read the settings for SQLAlchemy and
    # configure connection engine and session maker objects
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    pic_dir = settings['picture_directory']

    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    config = Configurator(settings=settings, session_factory=session_factory)


    config.add_route('favicon.ico', '/favicon.ico')
    # Serves static directory (ie. css, js, bootstrap, etc)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view(pic_dir,pic_dir)

    # Serves up home page
    config.add_route('home', '/')

    # Product Routes
    config.add_route('product', '/product/{id:\d+}/{slug}')
    config.add_route('product_action', '/product/{action}')

    # Cart Routes
    config.add_route('cart', '/cart')

    # Cart Routes
    config.add_route('checkout', '/checkout')


    # Sign authorization - added later
    config.add_route('auth', '/sign/{action}')


    config.scan()
    return config.make_wsgi_app()
