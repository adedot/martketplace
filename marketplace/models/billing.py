__author__ = 'owner'

from marketplace.models import *
from sqlalchemy import Column, String, Text, Integer


class Card(Base):
    __tablename__= "card"

    data = Column(Text)
    user_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    user = relationship('User', backref="card")
    num = Column(String(4))

    @property
    def display_number(self):
        return u'xxxxxxx-' + unicode(self.num)

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + self.display_number