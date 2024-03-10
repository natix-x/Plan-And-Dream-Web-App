from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, DataRequired, Email


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[Length(min=4, max=20), DataRequired()]
    )
    email_address = EmailField(
        "Email Address", validators=[Length(min=6, max=50), DataRequired(), Email()]
    )
    password1 = PasswordField(
        "Password",
        validators=[
            Length(min=6),
            DataRequired(),
            EqualTo("password2", message="Passwords must match"),
        ],
    )
    password2 = PasswordField("Repeat Password")
    submit = SubmitField("Create account")
