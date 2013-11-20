__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package

from sqlalchemy import (
    Column,
    String,
    DECIMAL,
    Boolean,
    Date,
    Integer,
    Text,
    )

product_category_table = \
    Table('product_categories', Base.metadata,
          Column('product_id', Integer, ForeignKey('product.id')),
          Column('category_id', Integer, ForeignKey('category.id'))
    )


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
    old_price = Column("old_price", DECIMAL(precision=9,scale=2),default=0.00)
    is_active = Column(Boolean,default=True)
    is_bestseller = Column(Boolean,default=False)
    is_featured = Column(Boolean,default=False)
    quantity = Column(Integer)
    description = Column(Text)
    meta_keywords = Column(String(255), unique=True) # Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = Column(String(255), unique=True) # Content for description meta tag
    created_at = Column(Date,default=datetime.datetime.utcnow)
    updated_at = Column(Date, default=datetime.datetime.utcnow)
    product_picture = Column(String(255))
    categories = relationship('Category', secondary=product_category_table, backref='products')

    @classmethod
    def all(cls):
        return DBSession.query(Product).order_by(sa.desc(Product.created_at))

    @classmethod
    def by_id(cls, id):
        return DBSession.query(Product).filter(Product.id == id).first()

    @property
    def slug(self):
        return urlify(self.name)


    @classmethod
    def get_paginator(cls, request, page=1):
        page_url = PageURL_WebOb(request)
        return Page(Product.all(), page, url=page_url, items_per_page=5)
