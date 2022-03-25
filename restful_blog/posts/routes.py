from cgitb import text
from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import current_user
from flask import current_app as app
from restful_blog.models import BlogPosts, db, Comments, Users, Categories
from restful_blog.forms import CreatePost, CommentsForm
from datetime import date
from functools import wraps

# Blueprint Configuration
posts_bp = Blueprint("posts_bp",
                     __name__,
                     template_folder="templates",
                     static_folder="static")


# Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated:
            return abort(403)
        elif current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


@posts_bp.route("/post/<int:index>", methods=["GET", "POST"])
def show_post(index):
    form = CommentsForm()
    post = BlogPosts.query.get(index)
    comments = Comments.query.filter_by(post_comment_id=index).all()
    if current_user.is_authenticated and request.method == "POST":
        add_comment_db = Comments(
            text=form.comment_body.data,
            post_comment_id=post.id,
            comment_user_id=current_user.id,
            comment_author=current_user.name,
        )
        db.session.add(add_comment_db)
        db.session.commit()
        return redirect(url_for("posts_bp.show_post", index=index))
    if not current_user.is_authenticated and request.method == "POST":
        error = "You need to be logged in to post comments."
        return redirect(url_for(
            "users_bp.login",
            error=error,
        ))
    return render_template("post.html",
                           post=post,
                           form=form,
                           comments=comments)


@posts_bp.route("/new-post", methods=["GET", "POST"])
@admin_only
def new_post():
    page_title = "New Post"
    t = date.today()
    author = current_user.name
    add_post_form = CreatePost(author=author)
    add_post_form.categories.choices = [(row.id, row.category)
                                        for row in Categories.query.all()]
    if request.method == "POST":
        add_post_db = BlogPosts(
            title=add_post_form.title.data,
            date=t.strftime("%B %d %Y"),
            body=add_post_form.body.data,
            author=add_post_form.author.data,
            img_url=add_post_form.img_url.data,
            author_id=current_user.id,
            post_category_id=add_post_form.categories.data[0],
        )
        db.session.add(add_post_db)
        db.session.commit()
        return redirect(url_for("home_bp.get_all_posts"))
    return render_template("make-post.html",
                           form=add_post_form,
                           title=page_title)


@posts_bp.route("/edit-post/<int:index>", methods=["GET", "POST"])
@admin_only
def edit_post(index):
    page_title = "Edit Post"
    post = BlogPosts.query.get(index)
    edit_form = CreatePost(
        title=post.title,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    edit_form.categories.choices = [(row.id, row.category)
                                    for row in Categories.query.all()]
    if request.method == "POST":
        post_edit = post
        post_edit.title = edit_form.title.data
        post_edit.body = edit_form.body.data
        post_edit.author = edit_form.author.data
        post_edit.img_url = edit_form.img_url.data
        post_edit.post_category_id = edit_form.categories.data[0]
        db.session.commit()
        return redirect(url_for("posts_bp.show_post", index=index))
    return render_template("make-post.html",
                           post=post,
                           title=page_title,
                           form=edit_form)


@posts_bp.route("/delete/<int:index>")
@admin_only
def delete_post(index):
    post_to_delete = BlogPosts.query.get(index)
    comments_to_delete = Comments.query.filter_by(post_comment_id=index).all()
    for comment in comments_to_delete:
        db.session.delete(comment)
        db.session.commit()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("home_bp.get_all_posts"))
