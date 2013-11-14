"""Add Category Table

Revision ID: 2cc82340240e
Revises: 437a4b30c3c2
Create Date: 2013-11-10 18:55:41.258387

"""

# revision identifiers, used by Alembic.
revision = '2cc82340240e'
down_revision = '437a4b30c3c2'


from alembic import op
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Text, Date

def upgrade():
    op.create_table(
        'category',
        Column('id', Integer, primary_key=True),
        Column('name', String(255)),
        Column('slug', String(255)),
        Column('is_active', Boolean, default=True),
        Column('description', Text),
        Column('meta_keywords', String(255)),
        Column('meta_description', String(255)),
        Column('created_at', Date),
        Column('updated_at', Date),
    )



def downgrade():
    op.drop_table('category')