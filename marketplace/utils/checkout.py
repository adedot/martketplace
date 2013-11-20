__author__ = 'owner'

import braintree
from marketplace.models.checkout import Order, OrderItem
from marketplace.utils import cart

from datetime import datetime


braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    "cn92b7xdrk4bgzwn",
    "2jzzb8hxjsj4jbgw",
    "4023624c52e3f5413490a53884e449e3"
)

amount = "1000.00"
credit_card_number = "4111111111111111"
expiration_month = "05"
expiration_year = "2012"


#result = braintree.Transaction.sale({
#    "amount": amount,
#    "credit_card": dict(number=credit_card_number, expiration_month=expiration_month, expiration_year=expiration_year)
#})
#
#
#
#
#if result.is_success:
#    print "success!: " + result.transaction.id
#elif result.transaction:
#    print "Error processing transaction:"
#    print "  message: " + result.message
#    print "  code:    " + result.transaction.processor_response_code
#    print "  text:    " + result.transaction.processor_response_text
#else:
#    print "message: " + result.message
#    for error in result.errors.deep_errors:
#        print "attribute: " + error.attribute
#        print "  code: " + error.code
#        print "  message: " + error.message


def process(request):
    """ takes a POST request containing valid order data; pings the payment gateway with the billing
    information and returns a Python dictionary with two entries: 'order_number' and 'message' based on
    the success of the payment processing. An unsuccessful billing will have an order_number of 0 and an error message,
    and a successful billing with have an order number and an empty string message.

    """
    # Transaction results
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'

    postdata = request.POST.copy()
    credit_card_number = postdata.get('credit_card_number', '')
    expiration_month = postdata.get('credit_card_expire_month', '')
    expiration_year = postdata.get('credit_card_expire_year', '')
    exp_date = expiration_month + expiration_year
    cvv = postdata.get('credit_card_cvv', '')
    amount = cart.cart_subtotal(request)

    response = braintree.Transaction.sale({
        "amount": amount,
        "credit_card": dict(number=credit_card_number, expiration_month=expiration_month,
                            expiration_year=expiration_year)
    })
    if response.is_success:
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        results = {'order_number': order.id, 'message': u''}
    if response.transaction:
        results = {'order_number': 0, 'message': response.message, 'code': response.transaction.processor_response_code,
                   'text': response.transaction.processor_response_text}
    else:
        results = {'order_number': 0, 'message':response.message, 'errors': response.errors}
    return results


def create_order(request, transaction_id):
    """ if the POST to the payment gateway successfully billed the customer, create a new order
    containing each CartItem instance, save the order with the transaction ID from the gateway,
    and empty the shopping cart

    """
    order = Order(request.POST)

    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()

    if order.pk:
        """ if the order save succeeded """
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            """ create order item for each cart item """
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price  # now using @property
            oi.product = ci.product

        # all set, clear the cart
        cart.empty_cart(request)

        ## save profile info for future orders
        #if request.user.is_authenticated():
        #    from ecomstore.accounts import profile
        #
        #    profile.set(request)

    return order


month_choice = []
# month_choice.append(('','- Month -'))
for i in range(1, 13):
    if len(str(i)) == 1:
        numeric = '0' + str(i)
    else:
        numeric = str(i)
    month_choice.append((numeric, datetime(2009, i, 1).strftime('%B')))
MONTHS = tuple(month_choice)

calendar_years = []
# calendar_years.append(('','- Year -'))
for i in range(datetime.now().year, datetime.now().year + 10):
    calendar_years.append((i, i))
YEARS = tuple(calendar_years)


def cc_expire_years():
    """ list of years starting with current twelve years into the future """
    current_year = datetime.datetime.now().year
    years = range(current_year, current_year + 12)
    return [(str(x), str(x)) for x in years]


def cc_expire_months():
    """ list of tuples containing months of the year for use in credit card form.
    [('01','January'), ('02','February'), ... ]

    """
    months = []
    for month in range(1, 13):
        if len(str(month)) == 1:
            numeric = '0' + str(month)
        else:
            numeric = str(month)
        months.append((numeric, datetime.date(2009, month, 1).strftime('%B')))
    return months


def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a Luhn mod-10 checksum
    Taken from: http://code.activestate.com/recipes/172845/

    """
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
    return ( (sum % 10) == 0 )