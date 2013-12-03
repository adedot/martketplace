__author__ = 'owner'

from datetime import datetime, timedelta
import decimal
import random
from marketplace.models.cart_item import CartItem
from marketplace.models import *

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    """ get the current user's cart id, sets new one if blank;
    Note: the syntax below matches the text, but an alternative,
    clearer way of checking for a cart ID would be the following:

    if not CART_ID_SESSION_KEY in request.session:

    """
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    """ function for generating random cart ID values """
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def get_cart_items(request):
    """ return all items from the current user's cart """
    return DBSession.query(CartItem).filter(CartItem.cart_id ==_cart_id(request))

def get_single_item(request, item_id):
    return DBSession.query(CartItem).filter(CartItem.cart_id ==_cart_id(request), CartItem.product_id == item_id)

# update quantity for single item
def update_cart(request):
    """ function takes a POST request that updates the quantity for single product instance in the
    current customer's shopping cart

    """
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        print "Update item", item_id
        print "quantity:", quantity
        if int(quantity) > 0:
            cart_item.update({"quantity":quantity})
            #cart_item.quantity = int(quantity)
        else:
            remove_from_cart(request)

# remove a single item from cart
def remove_from_cart(request):
    """ function that takes a POST request removes a single product instance from the current customer's
    shopping cart
    """
    postdata = request.POST.copy()
    item_id = postdata['item_id']

    cart_item = get_single_item(request, item_id)
    if cart_item:
        cart_item.delete()

def add_to_cart(request, product):
    """ function that takes a POST request and adds a product instance to the current customer's shopping cart """
    postdata = request.POST.copy()

    ## get product slug from post data, return blank if empty
    #product_slug = postdata.get('product_slug','')
    # get quantity added, return 1 if empty
    quantity = postdata.get('quantity',1)

    #get products in cart
    cart_products = get_cart_items(request)


    product_in_cart = False
    # check to see if item is already in cart
    for cart_item in cart_products:
        print "cart item is in cart"
        if cart_item.product.id == product.id:
            # update the quantity if found
            print "We are updating the quantity"
            cart_item.augment_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        # create and save a new cart item\
        print "Creating and saving new cart item"
        ci = CartItem()
        ci.product = product
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)

def cart_subtotal(request):
    """ gets the subtotal for the current shopping cart """
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)

    print "The number of products is", cart_products.count()

    print "The products are ", [x.product for x in cart_products]
    for cart_item in cart_products:
        print "I am here", cart_item.product.id
        print cart_item.product.price
        cart_total = cart_total + (cart_item.product.price * cart_item.quantity)
    return cart_total

# returns the total number of items in the user's cart
def cart_distinct_item_count(request):
    # check for items
    # if there are items, return the number
    return get_cart_items(request).count()
    # else return 0

def is_empty(request):
    return cart_distinct_item_count(request) == 0

def empty_cart(request):
    """ empties the shopping cart of the current customer """
    DBSession.query(CartItem).filter(CartItem.cart_id ==_cart_id(request)).delete()
    DBSession.flush()

#def remove_old_cart_items():
#    """ 1. calculate date of 90 days ago (or session lifespan)
#    2. create a list of cart IDs that haven't been modified
#    3. delete those CartItem instances
#
#    """
#    print "Removing old carts"
#    remove_before = datetime.now() + timedelta(days=-settings.SESSION_COOKIE_DAYS)
#    cart_ids = []
#    old_items = CartItem.objects.values('cart_id').annotate(last_change=Max('date_added')).filter(last_change__lt=remove_before).order_by()
#    for item in old_items:
#        cart_ids.append(item['cart_id'])
#    to_remove = CartItem.objects.filter(cart_id__in=cart_ids)
#    to_remove.delete()
#    print str(len(cart_ids)) + " carts were removed"

