from wtforms import Form
from wtforms import TextField, DecimalField, FileField, IntegerField, BooleanField
from wtforms.ext.appengine.db import model_form
from wtforms.validators import Required
from wtforms.ext.csrf import SecureForm
from hashlib import md5
from wtforms import validators
from models import Product
import re


class SearchForm(Form):
	query = TextField('query', [Required()])

class ProductAddForm(Form):
    name = TextField('name', [Required()])
    brand = TextField('brand', [Required()])
    sku =  TextField('sku', [Required()])
    price = DecimalField('price', [Required()])
    is_active = BooleanField('is_active')
    is_bestseller = BooleanField('is_active')
    is_featured = BooleanField('is_active')
    quantity = IntegerField('quantity', [Required()])
    description =  TextField('name', [Required()])
    meta_keywords =  TextField('name')
    meta_description =  TextField('name')
    product_picture = FileField(u'Profile Picture')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class ProductViewForm(Form):
	pass

class CartForm(Form):
	pass



class CheckoutForm(Form):
	pass

class BillingForm(Form):
	pass

