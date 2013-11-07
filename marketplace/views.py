from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import get_renderer

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Product
    )


class ProductViews(object):
    def __init__(self, request):
        self.request = request
        renderer = get_renderer("templates/layout.pt")
        self.layout = renderer.implementation().macros['layout']



    @view_config(route_name='home', renderer='templates/index.pt')
    def my_view(request):
    #try:
    #    one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    #except DBAPIError:
    #    return Response(conn_err_msg, content_type='text/plain', status_int=500)

    # Featured Products
        products = [
            {
                'name': "Vitamin C"
            },
            {
                'name': 'Vitamin D'
            },
            {
                'name': 'Chin Chin'
            },
            {
                'name': 'Cake'
            }]

        return dict(title="Okada MarketPlace", products=products)


