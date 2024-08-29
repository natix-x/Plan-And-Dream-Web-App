from app import db
from app.blueprints.user_page import user_page
from app.blueprints.user_page.form import ListItem
from database.models.lists import Lists
from database.models.todo import ThingsToDo
from flask import render_template, request, jsonify, redirect, url_for, abort
from flask_login import login_required, current_user, login_manager, AnonymousUserMixin


@user_page.route("/user_page/<username>/", methods=["GET", "POST"])
@login_required
def user_page_view(username):
    """
    if user is logged gives him possibility to add new list titles and things to particular lists
    :param username: entered nickname after /user_page/
    :return: user_page (unique for every user)
    """
    if username != current_user.username:
        return abort(401, description="You have to log in.")

    list_title = ListItem()  # create ListTitle object named 'list title'
    thing_to_do = ListItem()  # create ListItem object named 'thing_to_do'

    user_lists = Lists.query.filter_by(
        user_id=current_user.id
    ).all()  # return all list titles belonging to current user

    return render_template(
        "user_page/user_page.html",
        list_title=list_title,
        thing_to_do=thing_to_do,
        user_lists=user_lists,
        ThingsToDo=ThingsToDo,
    )


@user_page.route("/change_thing_status/<int:thing_id>/", methods=["POST"])
@login_required
def change_thing_status(thing_id):
    """
    changes the status of 'done' column in 'thingstodo' table in database:
        - done equal to True if list item crossed out on website and according checkbox is checked;
        - done equal to False if list item not crossed out on website and according checkbox is not checked
    :param thing_id: primary key of item in 'thingstodo' table
    :return: JSON-formatted data with status of the thingtodo
    """

    thing_item = ThingsToDo.query.get(thing_id)
    thing_status = request.form.get("thing_status")

    if thing_status == "done":
        thing_item.done = True
    elif thing_status == "undone":
        thing_item.done = False

    db.session.commit()
    return jsonify({"thing_item_status": thing_item.done}), 200


@user_page.route("/change_list_status/<int:list_id>/", methods=["POST"])
@login_required
def change_list_status(list_id):
    """
    changes the status of 'done' column in 'lists' table:
        - done equal to True if list item crossed out on website and according checkbox is checked;
        - done equal to False if list item not crossed out on website and according checkbox is not checked,
    also changes the status of 'done' column of associated tasks in 'thingstodo' table
    :param list_id: primary key of item in 'lists' table
    :return: JSON-formatted data with status of the list 
    """
    list_item = Lists.query.get(list_id)
    list_status = request.form.get("list_status")

    if list_status == "done":
        list_item.done = True
        for thing in list_item.things_on_the_list:
            thing.done = True
    elif list_status == "undone":
        list_item.done = False
        for thing in list_item.things_on_the_list:
            thing.done = False

    db.session.commit()
    return jsonify({"list_item_status": list_item.done}), 200
