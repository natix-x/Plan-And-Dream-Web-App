from configuration import Config
from database import db, ma
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # Flask instance creation
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# defined directory for database: "Plan-And-Dream-Web-App"
db.init_app(app)  # connect database and app
ma.init_app(app)  # connect marshmallow and app

# from app.cli.db_config import db_create, db_drop

# blueprints imports and registration

from app.blueprints.home import home
from app.blueprints.auth.register import register
from app.blueprints.auth.login import login
from app.blueprints.user_page import user_page
from app.blueprints.db_models.lists import lists
from app.blueprints.db_models.things_to_do import things_to_do
from app.blueprints.db_models.users import users


app.register_blueprint(home)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(user_page)
app.register_blueprint(lists)
app.register_blueprint(things_to_do)
app.register_blueprint(users)
