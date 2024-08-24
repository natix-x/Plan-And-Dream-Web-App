"""
handles adding and deleting items in 'thingstodo' table from db
"""

from flask import Blueprint

things_to_do = Blueprint("things_to_do", __name__)

from app.blueprints.db_models.things_to_do import routes
