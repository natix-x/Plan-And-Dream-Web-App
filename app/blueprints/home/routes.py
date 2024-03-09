from app.blueprints.home import home
from flask import render_template


@home.route('/', methods=["GET", "POST"])
@home.route('/home', methods=["GET", "POST"])
def main_view():
    return render_template("home.html")
