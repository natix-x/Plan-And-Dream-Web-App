from app.blueprints.user_page import user_page
from app import app, db
from flask import render_template, request, abort, redirect, url_for
from database.models.lists import Lists
from database.models.todo import ThingsToDo
from flask_login import login_required, current_user
from app.blueprints.user_page.form import ListItem


@user_page.route("/user_page/<username>", methods=["GET", "POST"])
@login_required
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
        "user_page.html",
        list_title=list_title,
        thing_to_do=thing_to_do,
        user_lists=user_lists,
        ThingsToDo=ThingsToDo,
    )


@user_page.route("/add_list_title/<int:user_id>", methods=["POST"])
@login_required
def add_list_title(user_id):
    """
    adds new lists for particular user defined by his id
    :param user_id: primary key of current user
    :return: updated database with added new list to Lists table
    """
    list_title = ListItem()

    if list_title.validate_on_submit():
        new_item = Lists(text=list_title.text.data, user_id=user_id)
        db.session.add(new_item)
        db.session.commit()

    return redirect(url_for("user_page.user_page_view", username=current_user.username))


@user_page.route("/add_thing_todo/<int:list_id>", methods=["POST"])
@login_required
def add_thing_todo(list_id):
    """
    adds things to particular lists based on specific list_id
    :param list_id: primary key of chosen list
    :return: updated database with added new thing to ThingsToDo table
    """
    list_title = Lists.query.get(list_id)

    thing_to_do = ListItem()
    if thing_to_do.validate_on_submit():
        new_thing = ThingsToDo(text=thing_to_do.text.data, list_id=list_title.id)
        db.session.add(new_thing)
        db.session.commit()

    return redirect(url_for("user_page.user_page_view", username=current_user.username))
