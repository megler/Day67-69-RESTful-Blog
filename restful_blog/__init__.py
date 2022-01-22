"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_gravatar import Gravatar
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from dotenv import load_dotenv
from os import environ, path

db = SQLAlchemy()
ckeditor = CKEditor()
login_manager = LoginManager()
csrf = CSRFProtect()

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    Bootstrap(app)
    ckeditor.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    gravatar = Gravatar(
        app,
        size=50,
        rating="g",
        default="retro",
        force_default=False,
        force_lower=False,
        use_ssl=False,
        base_url=None,
    )

    @login_manager.user_loader
    def load_user(id):
        """Login Manager For Flask-Login"""
        return Users.query.get(int(id))

    with app.app_context():
        # Import parts of our application
        from .users import routes
        from .posts import routes
        from .home import routes
        from .models import BlogPosts, Users, Comments

        engine = create_engine(
            environ.get("DATABASE_URL1", "sqlite:///posts.db"))
        if database_exists(engine.url) == False:
            db.create_all()

        # Register Blueprints
        app.register_blueprint(users.routes.users_bp)
        app.register_blueprint(posts.routes.posts_bp)
        app.register_blueprint(home.routes.home_bp)

        return app
