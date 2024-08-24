from app.blueprints.db_models.things_to_do import things_to_do
from app import app, db
from flask import jsonify, request
from flask_login import login_required
from database.models.todo import ThingsToDo, thing_to_do_schema, things_to_do_schema


@login_required
@things_to_do.route("/add_thing_to_do/<int:list_id>/", methods=["POST"])
def add_thing_to_do(list_id):
    """
    adds new thing to 'thingstodo' table in db
    :param list_id: primary key of chosen list to which added thing belongs
    :return: JSON formatted data, if successfully added: success: True and json object of added thing attributes,
    else: success: False
    """
    text = request.form.get("text")
    if text:
        new_item = ThingsToDo(text=text, list_id=list_id)
        db.session.add(new_item)
        db.session.commit()  # add new thing to 'thingstodo' table in db

        return jsonify({"success": True, "new_item": thing_to_do_schema.dump(new_item)}), 200

    return jsonify({"success": False}), 404


@login_required
@things_to_do.route("/delete_things_to_do/<int:list_id>/", methods=["POST"])
def delete_things_to_do(list_id):
    """
    deletes all things to do associated with a list from 'thingstodo' table in db
    :param list_id: Primary key of list for which things to do will be deleted
    :return: JSON response indicating success or failure
    """

    things_to_deleted = ThingsToDo.query.filter_by(list_id=list_id)
    if things_to_deleted:
        things_to_deleted.delete()
        db.session.commit()
        return jsonify({"message": "All things to do associated with the list have been deleted."}), 200
    else:
        return jsonify({"message": "Things not found"}), 404


@login_required
@things_to_do.route("/delete_thing_to_do/<int:thing_id>/", methods=["POST"])
def delete_thing_to_do(thing_id):
    """
    deletes chosen thing to do from a chosen list
    :param thing_id: primary key of thing to do that is selected to be deleted
    :return: JSON response indicating success
    """
    thing_to_deleted = ThingsToDo.query.filter_by(id=thing_id)
    if thing_to_deleted:
        thing_to_deleted.delete()
        db.session.commit()
        return jsonify({"message": "Thing deleted successfully"}), 200
    else:
        return jsonify({"message": "Thing not found"}), 404
