from wtforms import Form, TextField, DecimalField, FileField, IntegerField, BooleanField, HiddenField
from wtforms.ext.appengine.db import model_form
from wtforms.validators import Required
from wtforms import validators
from marketplace.models.product import Product
import re

# used to remove all the whitespace from
# the beginning and end of our input
strip_filter = lambda x: x.strip() if x else None

class SearchForm(Form):
	query = TextField('query', [Required()])

class ProductAddForm(Form):
    name = TextField('name', [Required()],
                         filters=[strip_filter])
    brand = TextField('brand', [Required()],
                         filters=[strip_filter])
    sku =  TextField('sku', [Required()],
                         filters=[strip_filter])
    price = DecimalField('price', [Required()])
    is_active = BooleanField('is_active')
    is_bestseller = BooleanField('is_active')
    is_featured = BooleanField('is_active')
    quantity = IntegerField('quantity', [Required()])
    description =  TextField('description', [Required()],
                         filters=[strip_filter])
    meta_keywords =  TextField('meta_keywords',
                         filters=[strip_filter])
    meta_description =  TextField('meta_description',
                         filters=[strip_filter])
    product_picture = FileField(u'Profile Picture')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class ProductUpdateForm(ProductAddForm):
    id = HiddenField()


class AddProductToCartForm(Form):
	quantity = IntegerField('quantity', [Required()])


class CartForm(Form):
    pass

class CheckoutForm(Form):
	pass

class BillingForm(Form):
	pass

