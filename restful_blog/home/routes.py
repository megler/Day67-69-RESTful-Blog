from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app as app
from flask_login import current_user
from restful_blog.models import BlogPosts, Users, Comments
from mailjet_rest import Client

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
    api_key = app.config["API_KEY"]
    api_secret = app.config["API_SECRET"]
    """Contact Page"""
    if request.method == "POST":
        mailjet = Client(auth=(api_key, api_secret), version="v3.1")
        data = {
            "Messages": [{
                "From": {
                    "Email": request.form["email"],
                    "Name": request.form["name"],
                },
                "To": [{
                    "Email": "YOUR-EMAIL@EMAIL.COM",
                    "Name": "YOUR NAME"
                }],
                "Subject":
                "Contact Form From Flask",
                "TextPart":
                request.form["message"],
            }]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
        if result.status_code == 200:
            flash("Your email was sent. Someone will get back with you soon.")
            return redirect(url_for("home_bp.get_all_posts"))
    return render_template("contact.html")
