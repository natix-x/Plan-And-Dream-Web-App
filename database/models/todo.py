from app import db, ma


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

    class ThingToDoSchema(ma.Schema):
        """
        handler for creation schemas objects for easier conversion to json
        """
        class Meta:
            """
            stores table's columns name
            """
            fields = ('id', 'text', 'done', 'list_id')

    thing_to_do_schema = ThingToDoSchema()  # handles singular record
    things_to_do_schema = ThingToDoSchema(many=True)  # handles multiple record
