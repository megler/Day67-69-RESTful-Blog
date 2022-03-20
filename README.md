# change_blog Blog

A Blog application using Flask and SQLAlchemy. Python Bootcamp Day 67/69 - change_blog Blog

## Overview

You can see a working copy at [change_log](https://marceia-flask-blog.herokuapp.com/)

**NOTE:** Site is on a free Heroku server. Give it a minute to spin up and start.


This application started exploring [Flask Blueprints](https://hackersandslackers.com/flask-blueprints) and the [application factory](https://hackersandslackers.com/flask-application-factory). While this
creates a more complex application with a lot of moving parts, in the end the
code is more encapsulated and easier to scale.

The blog has how been updated to include:

1. User login and authentication
2. An admin panel that is protected with user authentication
3. A comments section
4. A working contact form
5. Contextual error messages
6. A relational database (Postgres in production)

For posts and edits, the admin is currently the first user in the database. Every other user is a
subscriber. The navigation menu will change if the user is an admin and logged in.
Further, only an admin can add/edit posts.

In the admin dashboard (flask-admin), the admin is defined as logged in user who
has a specific email address (saved in env file). 

Users must be logged in to save comments on any blog post.

The contact form utilized the [MailJet API](mailjet.com) to send emails from the
contact form.

## Usage

When the flask app is run via `flask run` the database will be generated automatically.
The first person to register as a user will be considered an admin. All subsequent
will be subscribers.

## Notes for Pushing To Heroku Instance

1. When you convert your database from SQLite to Postgres, Heroku will create a
   URL that starts with `postgres://` and as a result your database will not properly
   deploy.

A workaround that needs to be improved is to create a second ENV variable called
DATABASE_URL1, copy the Heroku generated postgres link and change to `postgresql://`.

2. There was a persistent CRSF issue in production that did not exist locally.
   The app would allow you to log in, but almost immediately log you back out again.
   It was finally narrowed down to the Procfile that Gunicorn uses. Procfile should be
   `web: gunicorn "restful_blog:create_app()" --preload`

The `"restful_blog:create_app()"` will help Gunicorn find the info it needs to
launch the application if you are using a blueprint layout. The `--preload` _should_
fix the CRSF issue.

Everything else spun up as expected on Heroku with no other special workarounds.

## License  

[MIT](https://choosealicense.com/licenses/mit/)
