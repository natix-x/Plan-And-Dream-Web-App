from app import db
from .todo import ThingsToDo


class Lists(db.Model):
    """
    defines table called "lists" that contains 4 columns:
    'id', 'text', 'done', 'user_id' defined as:
    id: primary key,
    text: "to do list"'s title,
    done: status of the list, if False: not all activities done, if True: all activities done,
    user_id: id of the owner of the particular list based on table "users".
    This model is related to 'ThingsToDO'
    """

    __tablename__ = "lists"
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(30))
    done = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    things_on_the_list = db.relationship("ThingsToDo", backref="list", lazy=True)
