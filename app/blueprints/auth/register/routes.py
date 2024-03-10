from app.blueprints.register import register
from app.blueprints.register.form import RegistrationForm
from flask import render_template, request, redirect, url_for, flash
from database.models.users import User
from app import db, bcrypt


@register.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():  # check if username already exists in db
            flash('Username already registered!', 'danger')
        if User.query.filter_by(email_address=form.email_address.data).first():  # check if email already exists in db
            flash("Email already registered!", 'danger')
        else:
            new_user = User(
                username=form.username.data,
                email_address=form.email_address.data,
                password_hash=bcrypt.generate_password_hash(form.password1.data).decode("utf-8"),  # hash inserted password
            )
            db.session.add(new_user)
            db.session.commit()  # add new user to db and commit changes
            flash('Account created successfully!', 'success')
            return redirect(url_for("user_page.user_page", username=new_user.username))  # redirect user to user's main page

    return render_template("register.html", form=form)
