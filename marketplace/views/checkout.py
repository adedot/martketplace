__author__ = 'owner'

from marketplace.views import *
from marketplace.forms.checkout import CheckoutForm
from marketplace.utils import cart, checkout
from marketplace.models import *
from marketplace.models.checkout import Order, OrderItem


class CheckoutViews(object):

    def __init__(self, request):
        self.request = request
        #Use base layout
        renderer = get_renderer("marketplace:templates/layout.mako")

    @view_config(route_name='checkout', renderer='marketplace:templates/checkout.mako')
    def show_checkout(self):

        request = self.request

        form = CheckoutForm()


        if cart.is_empty(request):
            return HTTPFound(location=self.request.route_url('cart'))
        if request.method == 'POST':
            postdata = request.POST.copy()
            form = CheckoutForm(postdata)
            if form.validate():
                response = checkout.process(request)
                order_number = response.get('order_number',0)
                error_message = response.get('message','')
                if order_number:
                    request.session['order_number'] = order_number
                    return HTTPFound(location=self.request.route_url('checkout_receipt'))
            else:
                error_message = u'Correct the errors below'
        #else:
        #    if request.user.is_authenticated():
        #        user_profile = profile.retrieve(request)
        #        form = CheckoutForm(instance=user_profile)
        #    else:
        #        form = CheckoutForm()


        return {'form':form, 'title':"Checkout"}

    @view_config(route_name='checkout_receipt', renderer='marketplace:templates/receipt.mako')
    def receipt(self):
        """ page displayed with order information after an order has been placed successfully """
        order_number = self.request.session.get('order_number','')
        if order_number:
            order = DBSession.query(Order).filter(id=order_number).first()
            order_items = DBSession.query(OrderItem).filter(order=order)
        else:
            return HTTPFound(location=self.request.route_url('cart'))
        return {"title":"Checkout Receipt", "order_items":order_items}