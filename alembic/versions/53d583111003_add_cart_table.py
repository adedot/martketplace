"""Add Cart Table

Revision ID: 53d583111003
Revises: 2cc82340240e
Create Date: 2013-11-10 21:21:45.480330

"""

# revision identifiers, used by Alembic.
revision = '53d583111003'
down_revision = '2cc82340240e'

from alembic import op
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Text, Date
from sqlalchemy.schema import ForeignKey

def upgrade():
    op.create_table(
        'cart_item',
        Column('cart_id', String(50)),
        Column('date_added', Date),
        Column('quantity', Integer, default=1),
        Column('product_id', Integer, ForeignKey('product.id'))
    )



def downgrade():
    op.drop_table('cart_item')