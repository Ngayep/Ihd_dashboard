from flask import Blueprint, render_template
""" The route module creates the main Blueprint
and a route for the index page.
The Blueprint is imported in the app/__init__.py module."""
main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Route for the index page.
It returns the index.html template."""
    return render_template('index.html')
