from app.blueprints.user_view import user_view
from app import app
from flask import render_template

@user_view.route("/user", methods=["GET"]) 
def user_page():
    return render_template("user_view.html")
