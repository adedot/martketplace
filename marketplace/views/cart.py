from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.renderers import get_renderer
from marketplace.forms import ProductAddForm, SearchForm, ProductUpdateForm, AddProductToCartForm
import os

from sqlalchemy.exc import DBAPIError

from marketplace.models import (
    DBSession
    )


class CartViews(object):
    # Add checkout
    # Add to cart

    def __init__(self, request):
        self.request = request
        #Use base layout
        renderer = get_renderer("marketplace:templates/layout.mako")

    #
    #@view_config(route_name="cart", match_param="add", renderer='marketplace/cart.mako')
    #def add_to_cart(self):
    #    id = int(self.request.params.get('id', -1))
    #    product = Product.by_id(id)
    #
    #    if not product:
    #        return HTTPNotFound()
    #    form = ProductUpdateForm(self.request.POST, product)
    #
    #    url = self.request.route_url('cart')
    #    return HTTPFound(url)
