from flask import Flask
from database import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)  # app instance creation
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///plananddream.db'
# defined directory for database: "Plan-And-Dream-Web-App"
db.init_app(app)  # connect database and app

from app.cli.db_config import db_create, db_drop
from app.cli.db_seed import db_seed

# blueprints imports and registration
from app.blueprints.home import home
from app.blueprints.auth.register import register
from app.blueprints.auth.login import login
from app.blueprints.user_page import user_page


app.register_blueprint(home)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(user_page)




