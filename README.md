# RESTful Blog

A Blog application using Flask and SQLAlchemy. Python Bootcamp Day 67/69 - RESTful Blog

## Usage

This application started exploring [Flask Blueprints](https://hackersandslackers.com/flask-blueprints) and the [application factory](https://hackersandslackers.com/flask-application-factory). While this
creates a more complex application with a lot of moving parts, in the end the
code is more encapsulated and easier to scale.

The blog has how been updated to include:

1. User login and authentication
2. A very basic admin function that needs to be fleshed out
3. A comments section
4. A working contact form
5. Contextual error messages
6. A relational database

The admin is currently the first user in the database. Every other user is a
subscriber. The navigation menu will change if the user is an admin and logged in.
Further, only an admin can add/edit posts.

Users must be logged in to save comments on any blog post.

The contact form utilized the [MailJet API](mailjet.com) to send emails from the
contact form.

## License

[MIT](https://choosealicense.com/licenses/mit/)
