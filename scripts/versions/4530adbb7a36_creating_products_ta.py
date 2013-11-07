"""creating products table

Revision ID: 4530adbb7a36
Revises: None
Create Date: 2013-11-06 22:06:19.522900

"""

# revision identifiers, used by Alembic.
revision = '4530adbb7a36'
down_revision = None

from alembic import op
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Text, Date


def upgrade():
    op.create_table(
        'product',
        Column('id', Integer, primary_key=True),
        Column('name', String(255)),
        Column('slug', String(255)),
        Column('brand', String(50)),
        Column('sku', String(50)),
        Column('price', DECIMAL(precision=9,scale=2)),
        Column('old_price', DECIMAL(precision=9,scale=2), default=0.0),
        Column('is_active', Boolean, default=True),
        Column('is_bestseller', Boolean, default=False),
        Column('is_featured', Boolean, default=False),
        Column('quantity', Integer),
        Column('description', Text),
        Column('meta_keywords', String(255), unique=True),
        Column('meta_description', String(255), unique=True),
        Column('created_at', Date),
        Column('updated_at', Date),
        Column('product_picture', String(255), unique=True),
    )



def downgrade():
    op.drop_table('product')