from app.blueprints.user_page import user_page
from app import app
from flask import render_template


@user_page.route("/user_page/<username>", methods=["GET"])
def user_page(username):
    return render_template("user_page.html")
