__author__ = 'owner'
from wtforms import Form, TextField, DecimalField, FileField, IntegerField, BooleanField, HiddenField,SelectMultipleField
from marketplace.forms import *
from marketplace.models.category import Category

# used to remove all the whitespace from
# the beginning and end of our input
strip_filter = lambda x: x.strip() if x else None

categories = Category.all()

# Creates list of values based on first value of category results tuple
categories = [value for (value, ) in categories]

category_tuple = () #Used for select list of categories

# Add tuple to a tuple of tuples
for name in categories:
    category_choice = (name, name)
    category_tuple = category_tuple + (category_choice,)



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
    image = FileField(u'product_image')

    categories = SelectMultipleField("categories", choices=category_tuple)

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class ProductUpdateForm(ProductAddForm):
    id = HiddenField()


class AddProductToCartForm(Form):
	quantity = IntegerField('quantity', [Required()])