from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class ListItem(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    submit = SubmitField("Add")
