from app.blueprints.auth.login import login
from app.blueprints.auth.forms import LoginForm
from flask import render_template, request, redirect, url_for, flash, session, abort
from app import login_manager, db
from database.models.users import Users
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import check_password_hash


@login_manager.user_loader
def load_user(user_id):
    """
    given user_id returns the associated User object
    :param user_id: user id to retrieve
    :return: User object
    """
    return Users.query.get(user_id)


@login.route("/login/", methods=["GET", "POST"])
def login_page():
    """
    displays login form and:
    if user is already registered and email and password match: redirect user to his unique page and
    displays success message;
    if user is already registered and email and password do not match or
    user is not registered: displays error message;
    :return: flash message
    """
    if current_user.is_authenticated:
        return abort(403, description="First you have to log out.")  # forbidden

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                session.permanent = True
                flash(f'Success! Now you are logged as {user.username}.', 'success')
                return redirect(url_for("user_page.user_page_view", username=current_user.username))  # redirect user to user's main page
            else:
                flash("Username and password don't match.", "danger")
        else:
            flash("Nickname does not exist.", "danger")

    return render_template("login/login.html", form=form)


@login.route("/logout/")
@login_required
def logout():
    """
    logs user out
    :return: flashed message 'You are logged out!'
    """
    logout_user()
    flash("You are logged out!", "danger")
    return redirect(url_for('home.home_page'))

