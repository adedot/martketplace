from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.renderers import get_renderer
from forms import ProductAddForm, SearchForm, ProductUpdateForm

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Product
    )


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
        return {'title': "View Product", 'product':product}

    @view_config(route_name='product_action', match_param='action=edit', renderer='marketplace:templates/productaddedit.mako')
    def product_edit(self):
        id = int(self.request.params.get('id', -1))
        print "Id is", id
        product = Product.by_id(id)

        print product.name
        if not product:
            return HTTPNotFound()
        form = ProductUpdateForm(self.request.POST, product)
        if self.request.method == 'POST' and form.validate():
            form.populate_obj(product)
            return HTTPFound(location=self.request.route_url('product', id=product.id,
                                                        slug=product.slug))
        return {'form':form, 'title':"Edit Product", 'action':self.request.matchdict.get('action')}

    @view_config(route_name='product_action', match_param='action=search', renderer='marketplace:templates/search.mako')
    def product_search(self):
        pass
