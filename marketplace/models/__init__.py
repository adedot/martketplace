__author__ = 'owner'

from sqlalchemy import (
    Column,
    String,
    DECIMAL,
    Boolean,
    Date,
    Integer,
    Text,
    )
import sqlalchemy as sa
from webhelpers.text import urlify #<- will generate slugs
from webhelpers.paginate import PageURL_WebOb, Page #<- provides pagination
from webhelpers.date import time_ago_in_words #<- human friendly dates

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
    )

import datetime
from sqlalchemy.schema import ForeignKey, Table
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_marketplace_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

product_category_table = \
    Table('product_categories', Base.metadata,
          Column('product_id', Integer, ForeignKey('product.id')),
          Column('category_id', Integer, ForeignKey('category.id'))
    )

