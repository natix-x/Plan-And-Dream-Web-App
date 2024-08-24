from app import db
from app.blueprints.db_models.lists import lists
from database.models.lists import Lists, list_schema
from flask import jsonify, request
from flask_login import login_required


@login_required
@lists.route("/add_list/<int:user_id>/", methods=["POST"])
def add_list(user_id):
    """
    adds new list to 'lists' table in db
    :param user_id: primary key of user to whom new list belongs
    :return: JSON formatted data, if successfully added: {success: True, "new_item":json object of added list attributes},
    else: {success: False}
    """
    text = request.form.get("text")

    if text:
        new_item = Lists(text=text, user_id=user_id)
        db.session.add(new_item)
        db.session.commit()

        return jsonify({"success": True, "new_item": list_schema.dump(new_item)})

    return jsonify({"success": False})


@login_required
@lists.route("/delete_list/<int:user_id>/", methods=["POST"])
def delete_list(list_id):
    """
    deletes list from 'lists' table in db
    :param list_id: primary key of list that will be deleted
    :return: redirection to things_to_do.delete_thing_to_do endpoint
    """
    list_to_delete = Lists.query.filter_by(id=list_id).first()
    if list_to_delete:
        db.session.delete(list_to_delete)
        db.session.commit()
        return jsonify({"message": "success"}), 200
    else:
        return jsonify({"error": "List not found"}), 404
