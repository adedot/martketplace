"""Add category column to product. Also add product category relationship table

Revision ID: 38dd5400d624
Revises: 53d583111003
Create Date: 2013-11-10 21:25:51.900538

"""

# revision identifiers, used by Alembic.
revision = '38dd5400d624'
down_revision = '53d583111003'

from alembic import op
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Text, Date
from sqlalchemy.schema import ForeignKey

def upgrade():
    op.create_table(
        'product_categories',
        Column('product_id', Integer, ForeignKey('product.id')),
        Column('category_id', Integer, ForeignKey('category.id'))
    )


def downgrade():
    op.drop_table('product_categories')