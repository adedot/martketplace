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
from ..models.users import User
from ..models.billing import Card
from ..models.product import Product
from ..models.category import Category


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

        category1 = Category(name='Household, Food, & Pets', is_active=True, description="", meta_keywords="", meta_description="")
        category2 = Category(name='Medicine & Health', is_active=True, description="", meta_keywords="", meta_description="")
        category3 = Category(name='Beauty', is_active=True, description="", meta_keywords="", meta_description="")
        category4 = Category(name='Baby & Mom', is_active=True, description="", meta_keywords="", meta_description="")
        category5 = Category(name='Vitamins', is_active=True, description="", meta_keywords="", meta_description="")
        category6 = Category(name='Diet & Fitness', is_active=True, description="", meta_keywords="", meta_description="")
        categories = [category1,category2, category3, category4, category5, category6]
        DBSession.add_all(categories)

        product_1 = Product(name="Vitamin C", categories=[category5])
        product_2 = Product(name="Vitamin D", categories=[category5])
        DBSession.add_all([product_1,product_2])
