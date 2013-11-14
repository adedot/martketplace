__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package




class CartItem(Base):

    """ One to One relationship with products"""
    __tablename__ = 'cart_item'

    cart_id = Column(String(50), primary_key=True)
    date_added = Column(Date, default=datetime.datetime.utcnow())
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product',  backref=backref("cart", uselist=False))

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        """ called when a POST request comes in for a Product instance already in the shopping cart """
        self.quantity = self.quantity + int(quantity)
