from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    SelectField,
    TextAreaField,
)
from wtforms.validators import DataRequired


class CreatePost(FlaskForm):

    title = StringField(label="Title", validators=[DataRequired()])
    categories = SelectField("Categories:",
                             validators=[DataRequired()],
                             id="select_category")
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    body = TextAreaField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class NewUserRegister(FlaskForm):
    user_fname = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class CommentsForm(FlaskForm):
    comment_body = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
