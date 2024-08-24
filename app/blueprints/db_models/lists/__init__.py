"""
handles adding and deleting items in 'lists' table from db
"""

from flask import Blueprint

lists = Blueprint("lists", __name__)

from app.blueprints.db_models.lists import routes