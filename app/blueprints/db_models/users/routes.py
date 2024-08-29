from app import db
from app.blueprints.db_models.users import users
from database.models.users import Users, user_schema, users_schema
from flask import jsonify, flash
from flask_login import login_required


@users.route("/add_user/", methods=["POST"])
def add_user(username, email_address, password):
    """
    adds new user to 'users' table in db
    :param username: username of user to be added
    :param email_address: email of user to be added
    :param password: password of user to be added
    :return: JSON formatted data, if successfully added: success: True and json object of added user attributes
    """
    if Users.query.filter_by(
        username=username
    ).first():  # check if username already exists in db
        return jsonify({"success": False, "error": "Username already registered!"}), 404
    elif Users.query.filter_by(
        email_address=email_address
    ).first():  # check if email aslready exists in db
        return jsonify({"success": False, "error": "Email already registered!"}), 404
    else:
        new_user = Users(
            username=username, email_address=email_address, password=password
        )

        db.session.add(new_user)
        db.session.commit()  # add new user to db and commit changes
        return jsonify({"success": True, "new_user": user_schema.dump(new_user)}), 200


@users.route("/delete_user/<int:user_id>/", methods=["POST"])
@login_required
def delete_user(user_id):
    """
    deletes user from 'users' table in db
    :param user_id: primary key of user that is selected to be deleted
    :return JSON response indicating success or failure
    """
    user_to_deleted = Users.query.get(user_id)
    if user_to_deleted:
        db.session.delete(user_to_deleted)
        db.session.commit()
        flash("Your account has been deleted.", "danger")
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
