from pyramid.response import Response
from marketplace.views import *
from marketplace.forms.product import ProductAddForm, SearchForm, ProductUpdateForm, AddProductToCartForm
import os

from marketplace.utils import cart

from marketplace.models import (
    DBSession
    )

from marketplace.models.product import Product

class ProductViews(object):
    def __init__(self, request):
        self.request = request
        #Use base layout
        renderer = get_renderer("marketplace:templates/layout.mako")

    @view_config(route_name='home', renderer='marketplace:templates/index.mako')
    def home_page(request):

    # Featured Products
        products = Product.all()

        return dict(title="Okada MarketPlace", products=products)

    @view_config(route_name='product_action', match_param='action=create', renderer='marketplace:templates/productaddedit.mako')
    def product_create(self):
        product = Product()
        form = ProductAddForm(self.request.POST)
        if self.request.method =="POST" and form.validate():

            if form.image.data:
                self.write_picture_to_file(form, product)

            form.populate_obj(product)
            DBSession.add(product)
            return HTTPFound(location=self.request.route_url('home'))
        return {'form':form, 'title':"Add Product",'action':self.request.matchdict.get('action')}

    @view_config(route_name='product', renderer='marketplace:templates/productview.mako')
    def product_view(self):
        id = int(self.request.matchdict.get('id', -1))
        product = Product.by_id(id)
        if not product:
            return HTTPNotFound()

        form = AddProductToCartForm(self.request.POST)

        if self.request.method =="POST" and form.validate():
            print "The number of items added is", form.quantity.data

            session = self.request.session
            cart.add_to_cart(self.request, product)

            # show cart url
            return HTTPFound(location=self.request.route_url('cart'))
        else:
            form = AddProductToCartForm()

        return {'title': "View Product", 'product':product}

    def write_picture_to_file(self, form, product):
        # Create new image file
        settings = self.request.registry.settings
        picture_directory = str(settings['picture_directory']).strip("\"")
        image_file = os.path.join(picture_directory, form.image.data.filename)
        # write image data to image file
        destination = open(image_file, 'wb+')
        for line in form.image.data.file:
            destination.write(line)
        destination.close()
        form.image.data = image_file
        product.image = form.image.data

    @view_config(route_name='product_action', match_param='action=edit', renderer='marketplace:templates/productaddedit.mako')
    def product_edit(self):
        id = int(self.request.params.get('id', -1))
        product = Product.by_id(id)

        if not product:
            return HTTPNotFound()
        form = ProductUpdateForm(self.request.POST, product)

        if self.request.method == 'POST' and form.validate():

            if form.image.data.filename:

                self.write_picture_to_file(form, product)

            form.populate_obj(product)
            return HTTPFound(location=self.request.route_url('product', id=product.id,
                                                        slug=product.slug))
        return {'form':form, 'title':"Edit Product", 'action':self.request.matchdict.get('action')}

    @view_config(route_name='product_action', match_param='action=search', renderer='marketplace:templates/search.mako')
    def product_search(self):

        products = Product.all()

        form = SearchForm()

        return {'form':form, 'title': "Search", 'products' :products }