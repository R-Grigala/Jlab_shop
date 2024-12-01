from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# from src.admin.base import SecureAdminIndexView


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()