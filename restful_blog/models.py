from flask_login import UserMixin
from sqlalchemy import ForeignKey
"""Data models."""
from . import db


class BlogPosts(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer,
                          db.ForeignKey("users.id"),
                          nullable=False)
    post_comments = db.relationship("Comments",
                                    backref="blog_posts",
                                    lazy=True)


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship("BlogPosts", backref="users", lazy=True)
    comments = db.relationship("Comments", backref="users", lazy=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment_user_id = db.Column(db.Integer,
                                db.ForeignKey("users.id"),
                                nullable=False)
    post_comment_id = db.Column(db.Integer,
                                db.ForeignKey("blog_posts.id"),
                                nullable=False)
    text = db.Column(db.String(250))
    comment_author = db.Column(db.String(250), nullable=False)
