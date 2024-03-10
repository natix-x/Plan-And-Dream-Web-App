from app.blueprints.register import register
from app.blueprints.register.form import RegistrationForm
from flask import render_template, request, redirect, url_for
from database.models.users import User
from app import db


@register.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password1.data,
        )
        db.session.add(new_user)

        db.session.commit()
        print("New user added successfully.")

        return redirect(url_for("home.home_page"))
    return render_template("register.html", form=form)
