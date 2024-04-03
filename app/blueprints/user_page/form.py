from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class ListItem(FlaskForm):
    text = StringField("text", validators=[DataRequired()])
    submit = SubmitField("Add")
