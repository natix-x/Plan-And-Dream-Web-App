from app.blueprints.auth.forms import RegistrationForm
from app.blueprints.auth.register import register
from app.blueprints.db_models.users.routes import add_user
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user


@register.route("/register/", methods=["GET", "POST"])
def register_page():
    """
    displays registration form and:
    if user is registered correctly log him in, displays success message and redirects him to user's unique page,
    else: displays error message
    :return: flash message
    """
    form = RegistrationForm()

    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        email_address = form.email_address.data
        password = form.password1.data

        result = add_user(
            username, email_address, password
        )  # add user to 'users' table in db

        if result["success"]:
            new_user = result["new_user"]
            login_user(new_user)
            flash(
                f"Account created successfully! You are now logged in as {new_user.username}.",
                "success",
            )
            return redirect(
                url_for("user_page.user_page_view", username=new_user.username)
            )
        else:
            flash(result["error"], "danger")
    return render_template("register/register.html", form=form)
