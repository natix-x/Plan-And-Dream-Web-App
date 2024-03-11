from app import db


class ToDo(db.Model):
    """
    defines "to do" table that contains two columns: text - for defining planned activity and
    complete - for marking if it is done or not
    """

    __tablename__ = "todo"
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
