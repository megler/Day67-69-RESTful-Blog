from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
import secrets


class MyBaseForm(FlaskForm):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = secrets.token_urlsafe(16)
        csrf_time_limit = timedelta(minutes=20)


class CreatePost(MyBaseForm):
    title = StringField(label="Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class NewUserRegister(MyBaseForm):
    user_fname = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(MyBaseForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class CommentsForm(MyBaseForm):
    comment_body = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
