import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
import datetime
from ..models import (
    DBSession,
    Base,

    )
from ..models.checkout import Order, OrderItem
from ..models.account import User, UserProfile
from ..models.product import Product
from ..models.category import Category
from ..models.cart_item import CartItem


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        category1 = Category(name='Wine', is_active=True, description="", meta_keywords="",
                             meta_description="")
        category2 = Category(name='Cakes', is_active=True, description="", meta_keywords="",
                             meta_description="")
        category3 = Category(name='Electronics', is_active=True, description="", meta_keywords="", meta_description="")

        categories = [category1, category2, category3]
        DBSession.add_all(categories)

        pic_dir = settings['picture_directory']

#hess-ecabernet-sauvignan-1.jpg
#mangan.jpg
#barbie-cake.jpg
#soccer-cake.jpg
#dummy-cake-ben10-2.jpg
#edna-cabernet-sauvignan.jpg
#Eminence.jpg
#hatteras-red.jpg

#SAM_0091 copy.jpg
#SAM_0110 copy.jpg
# SAM_0111 copy.jpg
#speaker.JPG
#Ikeja-20130430-00289.jpg



        product_1 = Product(name="Hess Cabernet Sauvignan", brand="Baker's World", sku="12321323", price=3400, is_active=True, quantity=None,
                            description="Hess ECabernet Sauvignan", image=pic_dir+"hess-ecabernet-sauvignan-1.jpg", categories=[category1])
        product_2 = Product(name="Edna Cabernet Sauvignan", brand="Baker's World", sku="4343243243", price=3200, is_active=True, quantity=None,
                            description="Edna Cabernet Sauvignan", image=pic_dir+"edna-cabernet-sauvignan.jpg", categories=[category1])
        product_3 = Product(name="Hatteras Red", brand="Baker's World", sku="555232323", price=3400, is_active=True, quantity=None,
                            description="Wine", image=pic_dir+"hatteras-red.jpg", categories=[category1])
        product_4 = Product(name="Eminence", brand="Baker's World", sku="3432432431", price=2100, is_active=True, quantity=None,
                            description="Eminence Wine", image=pic_dir+"Eminence.jpg", categories=[category1])
        product_5 = Product(name="Mangan Wine", brand="Baker's World", sku="59032332", price=4000, is_active=True, quantity=None,
                            description="Mangan Wine", image=pic_dir+"mangan.jpg", categories=[category1])
        product_6 = Product(name="Soccer Cake", brand="Baker's World", sku="645435433", price=3000, is_active=True, quantity=None,
                            description="Soccer Cake", image=pic_dir+"soccer-cake.jpg", categories=[category2])
        product_7 = Product(name="Barbie Cake", brand="Baker's World", sku="78983923", price=4500, is_active=True, quantity=None,
                            description="Barbie Cake", image=pic_dir+"barbie-cake.jpg", categories=[category2])
        product_8 = Product(name="Birthday Cake", brand="Baker's World", sku="899090323", price=6000, is_active=True, quantity=None,
                            description="Birthday Cake", image=pic_dir+"dummy-cake-ben10-2.jpg", categories=[category2])
        product_9 = Product(name="Chocolate Cake", brand="Baker's World", sku="549090323", price=4900, is_active=True, quantity=None,
                            description="Chocolate Cake", image=pic_dir+"chocolatecake.jpg", categories=[category2])
        product_10 = Product(name="Portable Power", brand="Baker's World", sku="102321323", price=3400, is_active=True, quantity=None,
                            description="Portable Power", image=pic_dir+"SAM_0091 copy.jpg", categories=[category3])
        product_11 = Product(name="Portable Speaker", brand="Baker's World", sku="112321323", price=3400, is_active=True, quantity=None,
                            description="Portable Speaker", image=pic_dir+"SAM_0110 copy.jpg", categories=[category3])
        product_12 = Product(name="Purple Portable Speaker", brand="Baker's World", sku="14343243243", price=3200, is_active=True, quantity=None,
                            description="Purple Portable Speaker", image=pic_dir+"SAM_0111 copy.jpg", categories=[category3])
        product_13 = Product(name="Blue Portable Speaker", brand="Baker's World", sku="3555232323", price=3400, is_active=True, quantity=None,
                            description="Blue Portable Speaker", image=pic_dir+"speaker.jpg", categories=[category3])
        product_14 = Product(name="Standard Bank Portable Power", brand="Baker's World", sku="43432432431", price=2100, is_active=True, quantity=None,
                            description="Standard Bank Portable Power", image=pic_dir+"Ikeja-20130430-00289.jpg", categories=[category3])
        products = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9]
        products.extend([product_10, product_11, product_12, product_13, product_14])
        DBSession.add_all(products)
