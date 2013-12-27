__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Unicode,
    )
# Add users


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def by_name(cls, name):
        return DBSession.query(User).filter(User.name == name).first()

    def verify_password(self, password):
        return self.password == password


# Add User Profiles