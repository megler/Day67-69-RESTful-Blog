from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app as app
from flask_login import current_user
from restful_blog.models import BlogPosts, Users, Comments
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os, requests

load_dotenv()
recaptcha = ()

# Blueprint Configuration
home_bp = Blueprint("home_bp",
                    __name__,
                    template_folder="templates",
                    static_folder="static")


@home_bp.route("/", methods=["GET"])
def get_all_posts():
    """Homepage"""
    posts = BlogPosts.query.order_by(BlogPosts.id.desc()).all()
    return render_template("index.html", posts=posts)


@home_bp.route("/about")
def about():
    """About Page"""
    return render_template("about.html")


@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    SENDGRID_API_KEY = app.config["SENDGRID_API_SECRET_KEY"]
    SENDGRID_EMAIL_SENDER = app.config["SENDGRID_EMAIL_SENDER"]
    print(SENDGRID_API_KEY)

    if request.method == "POST":
        sname = request.form["nameaksljf"]
        semail = request.form["emaillkjkl"]
        smessage = request.form["messagesdfg"]
        parameters = request.form
        recaptcha_passed = False
        recaptcha_response = parameters.get("g-recaptcha-response")
        message = Mail(
            from_email=SENDGRID_EMAIL_SENDER,
            to_emails=SENDGRID_EMAIL_SENDER,
            subject="Change_Blog Contact Form",
            html_content=f"From: {sname} at {semail}<br /> Message: {smessage}",
        )
        try:
            recaptcha_secret = app.config["RECAPTCHA_SECRET_KEY"]
            response = requests.post(
                f"https://www.google.com/recaptcha/api/siteverify?secret={recaptcha_secret}&response={recaptcha_response}"
            ).json()
            recaptcha_passed = response.get("success")
            print(recaptcha_passed)
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            if response.status_code >= 200 and response.status_code < 300:
                flash(
                    "Your email was sent. Someone will get back with you soon."
                )
                return redirect(url_for("home_bp.get_all_posts"))
        except Exception as e:
            print(e)
    return render_template("contact.html")
