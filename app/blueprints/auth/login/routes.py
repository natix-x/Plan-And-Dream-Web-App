from app.blueprints.auth.login import login
from app.blueprints.auth.forms import LoginForm
from flask import render_template, request, redirect, url_for, flash
from app import login_manager, db
from database.models.users import User
from flask_login import login_user
from flask_bcrypt import check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user, remember=True)
                flash(f'Success! Now you are logged as {user.username}.', 'success')
                return redirect(url_for("user_page.user_page", username=user.username))
            else:
                flash("Username and password don't match.", "danger")

    return render_template("login.html", form=form)
