from app.blueprints.auth.register import register
from app.blueprints.auth.forms import RegistrationForm
from flask import render_template, request, redirect, url_for, flash
from database.models.users import Users
from app import db, bcrypt
from flask_login import login_user


@register.route("/register/", methods=["GET", "POST"])
def register_page():
    """
    displays registration form and:
    if username and email is already registered displays error messages;
    else: creates new user, adds him to db (table 'users'), log him in, displays success message and redirect him to user unique page
    :return: flash message
    """
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        if Users.query.filter_by(username=form.username.data).first():  # check if username already exists in db
            flash('Username already registered!', 'danger')
        elif Users.query.filter_by(email_address=form.email_address.data).first():  # check if email already exists in db
            flash("Email already registered!", 'danger')
        else:
            new_user = Users(
                username=form.username.data,
                email_address=form.email_address.data,
                password=form.password1.data)
            db.session.add(new_user)
            db.session.commit()  # add new user to db and commit changes
            login_user(new_user)
            flash(f'Account created successfully! Now you are now logged as {new_user.username}.', 'success')
            return redirect(url_for("user_page.user_page_view", username=new_user.username))  # redirect user to user's main page

    return render_template("register/register.html", form=form)