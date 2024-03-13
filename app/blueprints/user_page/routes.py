from app.blueprints.user_page import user_page
from app import app, db
from flask import render_template, request
from database.models.lists import Lists
from flask_login import login_required, current_user
from app.blueprints.user_page.form import ListItem


@user_page.route("/user_page/<username>", methods=["GET", "POST"])
@login_required
def user_page(username):
    list_item = ListItem()
    if request.method == "POST" and list_item.validate_on_submit():
        new_item = Lists(
            text=list_item.title.data,  # add new_list title to the table 'lists'
            user_id=current_user.id,
        )
        db.session.add(new_item)
        db.session.commit()

    user_items = Lists.query.filter_by(
        user_id=current_user.id
    ).all()  # return all list titles belonging to current user

    return render_template("user_page.html", list_item=list_item, user_items=user_items)
