__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package
from sqlalchemy import (
    Column,
    String,
    Boolean,
    Date,
    Integer,
    Text,
    )


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    slug = Column('slug', String(255),
                  unique=True) # Unique value for product page URL, created automatically from name.
    is_active = Column(Boolean, default=True)
    description = Column(Text)
    meta_keywords = Column(String(255)) # Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = Column(String(255)) # Content for description meta tag
    created_at = Column(Date, default=datetime.datetime.utcnow)
    updated_at = Column(Date, default=datetime.datetime.utcnow)

    def __init__(self, name, is_active, description, meta_keywords, meta_description):
        self.name = name
        self.is_active = is_active
        self.description = description
        self.meta_keywords = meta_keywords
        self.meta_description = meta_description


    @classmethod
    def by_id(cls, id):
        return DBSession.query(Category).filter(Category.id == id).first()

    @classmethod
    def names(cls):
        return DBSession.query(Category.name).distinct()

    @property
    def slug(self):
        return urlify(self.name)