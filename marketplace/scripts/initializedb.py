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
from ..models.account import User
from ..models.billing import Card
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
        category1 = Category(name='Household, Food, & Pets', is_active=True, description="", meta_keywords="",
                             meta_description="")
        category2 = Category(name='Medicine & Health', is_active=True, description="", meta_keywords="",
                             meta_description="")
        category3 = Category(name='Vitamins', is_active=True, description="", meta_keywords="", meta_description="")
        category4 = Category(name='Diet & Fitness', is_active=True, description="", meta_keywords="",
                             meta_description="")
        categories = [category1, category2, category3, category4]
        DBSession.add_all(categories)

        pic_dir = settings['picture_directory']

        product_1 = Product(name="Vitamin C", brand="Davis Drug", sku="12321323", price=20.99, is_active=True, quantity=None,
                            description="Vitamin C", image=pic_dir+"vitaminc300.jpg", categories=[category2,category3])
        product_2 = Product(name="Vitamin D", brand="Davis Drug", sku="4343243243", price=20.99, is_active=True, quantity=None,
                            description="Vitamin D", image=pic_dir+"vitamind.jpg", categories=[category2,category3])
        product_3 = Product(name="Acetaminophen", brand="Davis Drug", sku="555232323", price=20.99, is_active=True, quantity=None,
                            description="Acetaminophen - Pain Reliever", image=pic_dir+"Acetaminophen.jpg", categories=[category2])
        product_4 = Product(name="Advil", brand="Davis Drug", sku="3432432431", price=20.99, is_active=True, quantity=None,
                            description="Advil", image=pic_dir+"advil.jpg", categories=[category2])
        product_5 = Product(name="Tylenol", brand="Davis Drug", sku="59032332", price=20.99, is_active=True, quantity=None,
                            description="Tylenol", image=pic_dir+"tylenol-now.jpg", categories=[category2])
        product_6 = Product(name="Chlorhexidine", brand="Davis Drug", sku="645435433", price=20.99, is_active=True, quantity=None,
                            description="Chlorhexidine", image=pic_dir+"Chlorhexidine-peridex.jpg", categories=[category2])
        product_7 = Product(name="Nystatin", brand="Davis Drug", sku="78983923", price=20.99, is_active=True, quantity=None,
                            description="Nystatin", image=pic_dir+"nystatin.jpg", categories=[category2])
        product_8 = Product(name="Cisapride", brand="Davis Drug", sku="899090323", price=20.99, is_active=True, quantity=None,
                            description="Cisapride", image=pic_dir+"cisapride.png", categories=[category1,category2])
        product_9 = Product(name="Vicodin", brand="Davis Drug", sku="900232333", price=20.99, is_active=True, quantity=None,
                            description="Vicodin", image=pic_dir+"Vicodin-adverse-effects2.jpg", categories=[category2])
        DBSession.add_all([product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8, product_9])
