from flask import Blueprint

user_view = Blueprint("user_view", __name__, template_folder="templates")

from app.blueprints.user_view import routes
