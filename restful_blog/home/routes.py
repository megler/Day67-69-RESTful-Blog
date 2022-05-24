from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app as app
from flask_login import current_user
from restful_blog.models import BlogPosts, Users, Comments
from flask_recaptcha import ReCaptcha
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()
recaptcha = ReCaptcha(app)

# Blueprint Configuration
home_bp = Blueprint("home_bp",
                    __name__,
                    template_folder="templates",
                    static_folder="static")


@home_bp.route("/", methods=["GET"])
def get_all_posts():
    """Homepage"""
    posts = BlogPosts.query.order_by(BlogPosts.date.desc()).all()
    return render_template("index.html", posts=posts)


@home_bp.route("/about")
def about():
    """About Page"""
    return render_template("about.html")


@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    SENDGRID_API_KEY = app.config["SENDGRID_API_KEY"]
    SENDGRID_EMAIL_SENDER = app.config["SENDGRID_EMAIL_SENDER"]
    captcha_confirm = ""  # Create empty message

    if request.method == "POST":
        sname = request.form["name"]
        semail = request.form["email"]
        smessage = request.form["message"]
        if recaptcha.verify():
            captcha_confirm = "Thanks for filling out the form!"
        else:
            captcha_confirm = "Please fill out the ReCaptcha!"
        message = Mail(
            from_email=SENDGRID_EMAIL_SENDER,
            to_emails=SENDGRID_EMAIL_SENDER,
            subject="Change_Blog Contact Form",
            html_content=f"From: {sname} at {semail}<br /> Message: {smessage}",
        )
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            if response.status_code == 200:
                flash(
                    "Your email was sent. Someone will get back with you soon."
                )
                return redirect(url_for("home_bp.get_all_posts"))
        except Exception as e:
            print(e)
    return render_template("contact.html", captcha_confirm=captcha_confirm)
