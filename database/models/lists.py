from app import db


class ToDo(db.Model):
    __tablename__ = "lists"
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
