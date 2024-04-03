"""
contains all components: routes, templates, static files and the others for
handling user activities on his unique user page
"""
from flask import Blueprint

user_page = Blueprint("user_page", __name__, template_folder="templates", static_folder="static")

from app.blueprints.user_page import routes
