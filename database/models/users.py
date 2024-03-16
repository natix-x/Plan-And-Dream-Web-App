from app import db
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from .lists import Lists


class User(db.Model, UserMixin):
    """
    defines table called "users" which contains 4 columns: id (primary key), username, email_address and password,
    this model is related to 'Lists'
    """

    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    lists = db.relationship("Lists", backref="user", lazy=True)

    def __init__(self, username, email_address, password):
        self.username = username
        self.email_address = email_address
        self.password = generate_password_hash(password).decode("utf-8")  # hash password
