"""
handles adding and deleting in 'users' table from db
"""

from flask import Blueprint

users = Blueprint("users", __name__)

from app.blueprints.db_models.users import routes
