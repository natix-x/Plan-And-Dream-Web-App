from flask import Blueprint

user_page = Blueprint("user_page", __name__, template_folder="templates")

from app.blueprints.user_page import routes
