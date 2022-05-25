# change_log Blog
#
# Python Bootcamp Day 67 - change_log Blog
# Usage:
#      A Blog application using Flask and SQLAlchemy.
#
# Marceia Egler January 18, 2022
"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv
import secrets

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask config variables."""

    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    TESTING = False
    SECRET_KEY = secrets.token_urlsafe(16)
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    WTF_CSRF_SECRET_KEY = secrets.token_urlsafe(16)
    FLASK_ADMIN_SWATCH = "cerulean"

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL1",
                                          "sqlite:///posts.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Sendgrid
    SENDGRID_API_SECRET_KEY = environ.get("SENDGRID_API_SECRET_KEY")
    SENDGRID_EMAIL_SENDER = environ.get("SENDGRID_EMAIL_SENDER")

    # reCaptcha
    RECAPTCHA_SITE_KEY = environ.get("RECAPTCHA_SITE_KEY")
    RECAPTCHA_SECRET_KEY = environ.get("RECAPTCHA_SECRET_KEY")
