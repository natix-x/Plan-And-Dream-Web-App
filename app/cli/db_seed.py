from app import db, app
from database.models.lists import ToDo
from database.models.users import User


@app.cli.command("db_seed")
def db_seed():
    first_thing = ToDo(text="Do something useful")
    db.session.add(first_thing)

    test_user = User(username="nw1", email_address="nat1@gmail.com", password_hash="1234")
    db.session.add(test_user)
    db.session.commit()
    print("Database seeded")

