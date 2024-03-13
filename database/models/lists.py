from app import db


class Lists(db.Model):
    """
    defines table called "lists" that contains 3 columns: id, text and user_id
    id: primary key
    text: "to do list"'s title
    user_id: id of the owner of the particular list based on table "users"
    """

    __tablename__ = "lists"
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
