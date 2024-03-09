from flask import Flask
from database import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///plananddream.db'
db.init_app(app)
from app.cli.db_config import db_create, db_drop
from app.cli.db_seed import db_seed

from app.blueprints.home import home
app.register_blueprint(home)


