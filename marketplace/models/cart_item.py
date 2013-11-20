__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package

from sqlalchemy import (
    Column,
    String,
    Date,
    Integer,
    )


class CartItem(Base):

    """ Many to One/One to Many relationship with products. Provides bidirectional behavior """
    __tablename__ = 'cart_item'

    cart_id = Column(String(50), primary_key=True)
    date_added = Column(Date, default=datetime.datetime.utcnow())
    quantity = Column(Integer)
    product_id = Column(Integer,  ForeignKey('product.id'),primary_key=True)
    product = relationship('Product', backref="cart_items") # Cart can have many products

    @property
    def total(self):
        return self.quantity * self.product.price

    @property
    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.slug

    def augment_quantity(self, quantity):
        """ called when a POST request comes in for a Product instance already in the shopping cart """
        self.quantity = self.quantity + int(quantity)
