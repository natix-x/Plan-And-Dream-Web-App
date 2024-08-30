from app import app, db
from database.models.lists import Lists
from database.models.lists import ThingsToDo
from database.models.users import Users


@app.cli.command("db_seed_users")
def db_seed_users():
    """
    Seeds 'users' table with test data
    """
    test_user1 = Users(
        username="test_user1", email_address="test_user1@test.com", password="test123"
    )
    test_user2 = Users(
        username="test_user2", email_address="test_user2@test.com", password="test123"
    )
    test_user3 = Users(
        username="test_user3", email_address="test_user3@test.com", password="test123"
    )
    db.session.add(test_user1)
    db.session.add(test_user2)
    db.session.add(test_user3)
    db.session.commit()
    print("Database seeded! 'users' table filled with test data.")


@app.cli.command("db_seed_lists")
def db_seed_lists():
    """
    Seeds 'lists' table with test data
    """
    test_list1 = Lists(text="test1", user_id=1)
    test_list2 = Lists(text="test2", user_id=2)
    test_list3 = Lists(text="test3", user_id=3)
    db.session.add(test_list1)
    db.session.add(test_list2)
    db.session.add(test_list3)
    db.session.commit()
    print("Database seeded! 'lists' table filled with test data.")


@app.cli.command("db_seed_things_to_do")
def db_seed_things_to_do():
    """
    Seeds 'thingstodo' table with test data
    """
    task1 = ThingsToDo(text="test1", list_id=1)
    task2 = ThingsToDo(text="test2", list_id=2)
    task3 = ThingsToDo(text="test3", list_id=3)
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.commit()
    print("Database seeded! 'thingstodo' table filled with test data.")
