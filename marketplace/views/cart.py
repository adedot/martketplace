from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.renderers import get_renderer
import os
from marketplace.utils import cart

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

    @view_config(route_name='cart', renderer='marketplace:templates/cart.mako')
    def show_cart(self):

        request = self.request

        if request.method == 'POST':
            postdata = request.POST.copy()
            if postdata['submit'] == 'Remove':
                cart.remove_from_cart(request)
            if postdata['submit'] == 'Update':
                cart.update_cart(request)
        #    if postdata['submit'] == 'Checkout':
        #        checkout_url = checkout.get_checkout_url(request)
        #        return HTTPFound(checkout_url)


        cart_subtotal = cart.cart_subtotal(request)
        print "Subtotal is ", cart_subtotal

        cart_items = cart.get_cart_items(request)

        print "The number of items is ",  cart_items.count()
        page_title = 'Shopping Cart'

        return {'title': page_title, 'cart_items':cart_items, 'cart_subtotal': cart_subtotal }

