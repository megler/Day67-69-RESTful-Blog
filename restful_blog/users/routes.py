from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask import current_app as app
from restful_blog.models import BlogPosts, db, Users, Comments
from restful_blog.forms import NewUserRegister, LoginForm
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint Configuration
users_bp = Blueprint("users_bp",
                     __name__,
                     template_folder="templates",
                     static_folder="static")

# @users_bp.route("/register", methods=["GET", "POST"])
# def register():
#     form = NewUserRegister()

#     if request.method == "POST" and form.validate_on_submit():
#         username = form.user_fname.data
#         email = form.email.data
#         password = generate_password_hash(form.password.data,
#                                           method="pbkdf2:sha256",
#                                           salt_length=8)
#         email_check = Users.query.filter_by(email=email).first()

#         if email_check != None:
#             if email == email_check.email:
#                 error = "There is already a user with this email. Perhaps you meant to log in?"
#                 return redirect(url_for(
#                     "users_bp.login",
#                     error=error,
#                 ))
#         else:
#             new_user = Users(
#                 name=username,
#                 email=email,
#                 password=password,
#             )
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user)
#             return redirect(url_for("home_bp.get_all_posts"))
#     return render_template("register.html", form=form)


@users_bp.route("/login/", methods=["GET", "POST"])
@users_bp.route("/login/<error>", methods=["GET", "POST"])
def login(error=None):
    form = LoginForm()
    """User Login."""
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.get_all_posts"))

    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = Users.query.filter_by(email=email).first()
            if not user:
                error = "Invalid email address. Please try again."
            elif not check_password_hash(user.password, password):
                error = "Invalid password. Please try again."
            else:
                flash("You were successfully logged in")
                login_user(user)
                return redirect(url_for("home_bp.get_all_posts"))

    return render_template("login.html", error=error, form=form)


@users_bp.route("/logout")
@login_required
def logout():
    """User logout."""
    logout_user()
    return redirect(url_for("home_bp.get_all_posts"))
