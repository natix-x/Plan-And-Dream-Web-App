from flask import Blueprint

register = Blueprint("register", __name__, template_folder="templates")

from app.blueprints.register import routes
