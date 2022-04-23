from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app as app
from flask_login import current_user
from restful_blog.models import BlogPosts, Users, Comments
from mailjet_rest import Client
import os

# Blueprint Configuration
home_bp = Blueprint("home_bp",
                    __name__,
                    template_folder="templates",
                    static_folder="static")


@home_bp.route("/", methods=["GET"])
def get_all_posts():
    """Homepage"""
    posts = BlogPosts.query.all()
    return render_template("index.html", posts=posts)


@home_bp.route("/about")
def about():
    """About Page"""
    return render_template("about.html")


@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    # api_key = app.config["API_KEY"]
    # api_secret = app.config["API_SECRET"]
    # """Contact Page"""
    # if request.method == "POST":
    #     sname = request.form["name"]
    #     semail = request.form["email"]
    #     smessage = request.form["message"]
    #     mailjet = Client(auth=(api_key, api_secret), version="v3.1")
    #     data = {
    #         "Messages": [{
    #             "From": {
    #                 "Email": os.environ["MJ_SENDER_EMAIL"],
    #                 "Name": "Marceia with Python Study Group",
    #             },
    #             "To": [{
    #                 "Email": os.environ["MJ_RECEIVER_EMAIL"],
    #                 "Name": "Marceia"
    #             }],
    #             "Subject":
    #             "Contact Form From Your blog",
    #             "TextPart":
    #             f"From: {sname}\nEmail: {semail}\nMessage: {smessage}",
    #         }]
    #     }
    #     result = mailjet.send.create(data=data)
    #     print(result.status_code)
    #     print(result.json())
    #     if result.status_code == 200:
    #         flash("Your email was sent. Someone will get back with you soon.")
    #         return redirect(url_for("home_bp.get_all_posts"))
    return render_template("contact.html")
