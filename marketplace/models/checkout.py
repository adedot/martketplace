__author__ = 'owner'

from sqlalchemy import (
    Column,
    DECIMAL,
    Integer,
    String, DateTime
    )
from sqlalchemy.orm import validates
import decimal
from marketplace.models import * # To use all the settings in the models package
from marketplace.models.product import Product
from marketplace.models.category import Category


class BaseOrderInfo(Base):
    __abstract__=  True

    # contact info
    email = Column(String(50))
    phone = Column(String(20))
    prescription_number = Column(String(30))


    #shipping information
    shipping_name = Column(String(50))
    shipping_address_1 = Column(String(50))
    shipping_address_2 = Column(String(50))
    shipping_city = Column(String(50))
    shipping_state = Column(String(2))
    shipping_country = Column(String(50))
    shipping_zip = Column(String(10))

    #billing information
    billing_name = Column(String(50))
    billing_address_1 = Column(String(50))
    billing_address_2 = Column(String(50))
    billing_city = Column(String(50))
    billing_state = Column(String(2))
    billing_country = Column(String(50))
    billing_zip = Column(String(10))

class Order(BaseOrderInfo):
    """ model class for storing a customer order instance """
    # each individual status
    __tablename__ = "order"

    SUBMITTED = 1
    PROCESSED = 2
    SHIPPED = 3
    CANCELLED = 4
    # set of possible order statuses
    ORDER_STATUSES = ((SUBMITTED,'Submitted'),
                      (PROCESSED,'Processed'),
                      (SHIPPED,'Shipped'),
                      (CANCELLED,'Cancelled'),)

    id = Column(Integer, primary_key=True)

    #order info
    date = Column(DateTime)
    status = Column(Integer(default=SUBMITTED))
    ip_address = Column(String(16))
    last_updated = Column(DateTime)
    #user_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    #user = relationship('User', backref="orders")
    transaction_id = Column(String(20), primary_key=True)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    @property
    def __unicode__(self):
        return u'Order #' + str(self.id)

    @property
    def total(self):
        total = decimal.Decimal('0.00')
        order_items = DBSession.query(OrderItem).filter(OrderItem.order_id==self.id).all()
        for item in order_items:
            total += item.total
        return total

    @property
    def get_absolute_url(self):
        return ('order_details', (), { 'order_id': self.id })

class OrderItem(Base):

    __tablename__ = "order_item"
    """ model class for storing each Product instance purchased in each order """

    product_id = Column(Integer,  ForeignKey('product.id'), primary_key=True)
    product = relationship('Product', backref="order_items") # Cart can have many products
    quantity = Column(Integer)
    price = Column(DECIMAL(precision=9,scale=2))
    order_id = Column(Integer,  ForeignKey('order.id'), primary_key=True)
    order = relationship('Order', backref="order_items")

    @property
    def total(self):
        return self.quantity * self.price

    @property
    def name(self):
        return self.product.name

    @property
    def sku(self):
        return self.product.sku
    @property
    def __unicode__(self):
        return self.product.name + ' (' + self.product.sku + ')'
    @property
    def get_absolute_url(self):
        return self.product.get_absolute_url()