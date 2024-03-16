from app import db


class ThingsToDo(db.Model):
    """
    defines table called "things to do" that contains 4 columns: 'id', 'text', 'done' and 'list_id' defined as:
    id: primary key,
    text: thing to be done in the future defined for particular list,
    done: status of activity, if False: not done, if True: done
    list_id: id of the list to which thing belongs to based on table "lists".
    """

    __tablename__ = "thingstodo"
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))
