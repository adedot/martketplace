__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package
from marketplace.models.checkout import BaseOrderInfo
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Unicode,
    )
# Add users
import cryptacular.bcrypt
from sqlalchemy.orm import synonym

crypt = cryptacular.bcrypt.BCRYPTPasswordManager()

def hash_password(password):
    return unicode(crypt.encode(password))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(Unicode(255), unique=True, nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    _password = Column('password', Unicode(60))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)


    def __init__(self, email, password ):
        self.email = email
        self.password = password
        self.last_logged = datetime.datetime.now()

    @classmethod
    def by_email(cls, email):
        return DBSession.query(User).filter(User.email == email).first()

    @classmethod
    def check_password(cls, username, password):
        user = cls.get_by_username(username)
        if not user:
            return False
        return crypt.check(user.password, password)




# Add User Profiles
class UserProfile(BaseOrderInfo):
    __tablename__ = 'user_profile'

    id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    user = relationship('User', backref="user_profiles")
