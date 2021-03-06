__author__ = 'owner'

import unittest
import transaction

from pyramid import testing

from marketplace.models import DBSession
from marketplace.models.product import Product

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from marketplace.models import (
            Base
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        #with transaction.manager:
        #    model = MyModel(name='one', value=55)
        #    DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()