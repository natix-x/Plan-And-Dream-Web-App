from app.blueprints.user_page import user_page
from app import app, db
from flask import render_template, request, abort, redirect, url_for, jsonify
from database.models.lists import Lists, list_schema, lists_schema
from database.models.todo import ThingsToDo
from flask_login import login_required, current_user
from app.blueprints.user_page.form import ListItem


@login_required
@user_page.route("/user_page/<username>/", methods=["GET", "POST"])
def user_page_view(username):
    """
    if user is logged gives him possibility to add new list titles and things to particular lists
    :param username: entered nickname after /user_page/
    :return: user_page (unique for every user) or HTTP 403 if user is not currently logged in
    """
    if username != current_user.username:
        abort(403)  # HTTP 403

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


@login_required
@user_page.route("/add_list_title/<int:user_id>/", methods=["POST"])
def add_list_title(user_id):

    text = request.form.get('text')

    if text:
        new_item = Lists(text=text, user_id=user_id)
        db.session.add(new_item)
        db.session.commit()

        return jsonify({"success": True, "new_item": list_schema.dump(new_item)})

    return jsonify({"success": False})


@login_required
@user_page.route("/add_thing_todo/<int:list_id>/", methods=["POST"])
def add_thing_todo(list_id):
    """
    adds things to particular lists based on specific list_id
    :param list_id: primary key of chosen list
    :return: updated database with added new thing to ThingsToDo table
    """

    thing_to_do = ListItem()
    if thing_to_do.validate_on_submit():
        new_thing = ThingsToDo(text=thing_to_do.text.data, list_id=list_id)
        db.session.add(new_thing)
        db.session.commit()  # add new thing to 'thingstodo' table in db

    return redirect(url_for("user_page.user_page_view", username=current_user.username))


@login_required
@user_page.route("/change_list_status/<int:list_id>/", methods=["POST"])
@user_page.route("/change_list_status/<int:thing_id>/", methods=["POST"])
def change_list_status(list_id=None, thing_id=None):
    """
    changes the status of 'done' column connected to provided list_id while changing 'lists' table
    or thing_id while changing 'things_todo' table:
    done equal to True if list item crossed out on website and according checkbox is checked;
    done equal to False if list item not crossed out on website and according checkbox is not checked
    :param list_id: primary key of item in 'lists' table
    :param thing_id: primary key of item in 'things_todo'
    :return: updated database with changed 'done' column
    """
    list_item = None

    if list_id is not None:
        list_item = Lists.query.get(list_id)
    elif thing_id is not None:
        list_item = ThingsToDo.query.get(thing_id)
    else:
        print("Invalid input")  # if both arguments None

    list_status = request.form.get("list_status")
    # get list_status from form in user_page.html: done if checkbox according to list item checked, else: undone

    if list_status == "done":
        list_item.done = True  # set done equal to True
    elif list_status == "undone":
        list_item.done = False  # set done equal to False

    db.session.commit()  # commit changes
    return redirect(url_for("user_page.user_page_view", username = current_user.username))
