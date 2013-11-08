marketplace README
==================

Getting Started
---------------

- cd <directory containing this file>

# Creates python package for development environment
- $venv/bin/python setup.py develop

# Run pyramid application with properties from development.ini
- $venv/bin/pserve --reload development.ini



# Uses python script to create and load data into tables (Optional)
- $venv/bin/initialize_marketplace_db development.ini

# Use alembic for database migrations.

alembic init alembic


alembic upgrade head