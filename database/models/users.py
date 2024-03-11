from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    defines table called "users" which contains 3 columns: username, email_address and password_hash
    """
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
