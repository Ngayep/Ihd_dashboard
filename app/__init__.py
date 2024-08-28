from flask import Flask
"""The create_app function creates a Flask application"""


def create_app():
    """Creates a Flask application"""
    app = Flask(__name__)
    from .routes import main
    app.register_blueprint(main)
    return app
