__author__ = 'owner'

from marketplace.models import * # To use all the settings in the models package

class Category(Base):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    slug = Column('slug', String(255), unique=True) # Unique value for product page URL, created automatically from name.
    is_active = Column(Boolean,default=True)
    description = Column(Text)
    meta_keywords = Column(String(255), unique=True) # Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = Column(String(255), unique=True) # Content for description meta tag
    created_at = Column(Date,default=datetime.datetime.utcnow)
    updated_at = Column(Date, default=datetime.datetime.utcnow)

    @property
    def slug(self):
        return urlify(self.name)