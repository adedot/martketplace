from sqlalchemy import (
    Column,
    String,
    DECIMAL,
    Boolean,
    Date,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

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

#Add Products

class Product(Base):
    """ model class containing information about a product; instances of this class are what the user
    adds to their shopping cart and can subsequently purchase

    """
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    slug = Column('slug', String(255), unique=True) # Unique value for product page URL, created automatically from name.
    brand = Column(String(50))
    sku = Column(String(50))
    price = Column(DECIMAL(precision=9,scale=2))
    old_price =  Column("old_price", DECIMAL(precision=9,scale=2),default=0.00)
    is_active = Column(Boolean,default=True)
    is_bestseller = Column(Boolean,default=False)
    is_featured = Column(Boolean,default=False)
    quantity = Column(Integer)
    description = Column(Text)
    meta_keywords = Column(String(255), unique=True) # Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = Column(String(255), unique=True) # Content for description meta tag
    created_at = Column(Date)
    updated_at = Column(Date)
    product_picture = Column(String(255))

    def __init__(self, name, slug, brand, sku, price, old_price, is_active, is_bestseller, is_featured, quantity, description,
                 meta_keywords, meta_description, created_at, update_at, product_picture):
        self.name = name
        self.slug = slug
        self.brand = brand
        self.sku = sku
        self.price = price
        self.old_price =old_price
        self.is_active = is_active
        self.is_bestseller = is_bestseller
        self.is_featured = is_featured
        self.quantity = quantity
        self.description = description
        self.meta_keywords = meta_keywords
        self.meta_description = meta_description
        self.created_at = created_at
        self.updated_at = update_at
        self.product_picture = product_picture



#Index('my_index', MyModel.name, unique=True, mysql_length=255)
