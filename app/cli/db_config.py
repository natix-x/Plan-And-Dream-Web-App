from app import app, db


@app.cli.command("db_create")
def db_create():
    """
    creates a database and the files that store the database
    :return: db files and message if successful
    """
    db.create_all()
    print("Database created!")


@app.cli.command("db_drop")
def db_drop():
    """
    drops all tables in the database and deletes the database
    :return: message if successful
    """
    db.drop_all()
    print("Database dropped!")

