__author__ = 'owner'

from marketplace.views import *

from marketplace.models import (
    DBSession
    )

from marketplace.models.product import Product
from marketplace.models.category import Category



class CategoryViews(object):

    def __init__(self, request):
        self.request = request
        #Use base layout
        renderer = get_renderer("marketplace:templates/layout.mako")

    @view_config(route_name='category', renderer='marketplace:templates/category/categoryview.mako')
    def category_view(self):
        id = int(self.request.matchdict.get('id', -1))
        category = Category.by_id(id)

        print "The Category is: ", category.name
        products = DBSession.query(Product).filter(Product.categories.any(Category.name==category.name)).all()

        return dict(title="Okada MarketPlace", category=category.name, products=products)
