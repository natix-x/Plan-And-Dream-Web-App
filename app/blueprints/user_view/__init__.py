from flask import Blueprint

user_view = Blueprint("home",
                 __name__,
                 template_folder='templates')

from app.blueprints.user_view import user_view