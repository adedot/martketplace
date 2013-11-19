__author__ = 'owner'

from marketplace.views import *
from marketplace.forms.checkout import CheckoutForm

class CheckoutViews(object):

    def __init__(self, request):
        self.request = request
        #Use base layout
        renderer = get_renderer("marketplace:templates/layout.mako")

    @view_config(route_name='checkout', renderer='marketplace:templates/checkout.mako')
    def show_checkout(self):

        request = self.request

        form = CheckoutForm()

        return {'form':form, 'title':"Checkout"}