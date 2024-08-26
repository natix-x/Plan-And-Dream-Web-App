from app import db
from app.blueprints.db_models.users import users
from database.models.users import Users
from flask import jsonify
from flask_login import login_required


@users.route("/add_user/", methods=["POST"])
def add_user(username, email_address, password):
    if Users.query.filter_by(
        username=username
    ).first():  # check if username already exists in db
        return {"success": False, "error": "Username already registered!"}
    elif Users.query.filter_by(
        email_address=email_address
    ).first():  # check if email already exists in db
        return {"success": False, "error": "Email already registered!"}
    else:
        new_user = Users(
            username=username, email_address=email_address, password=password
        )

        db.session.add(new_user)
        db.session.commit()  # add new user to db and commit changes
        return {"success": True, "new_user": new_user}


@login_required
@users.route("/delete_user/<int:user_id>/", methods=["POST"])
def delete_user(user_id):
    """
    deletes user from 'users' table in db
    :param user_id: primary key of user that is selected to be deleted
    :return JSON response indicating success or failure
    """
    user_to_delted = Users.query.filter_by(id=user_id)
    if user_to_delted:
        user_to_delted.delete()
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
