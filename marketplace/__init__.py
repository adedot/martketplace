from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.view import static

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    config.add_route('favicon.ico', '/favicon.ico')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # Product Routes
    config.add_route('product_search', '/product/search')
    config.add_route('product_create', '/product/create')
    config.add_route('product_view', '/product/view/{id}')
    config.add_route('product_edit', '/product/edit/{id}')
    config.scan()
    return config.make_wsgi_app()
