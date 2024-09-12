from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Creates a Flask application"""
    app = Flask(__name__)

    # Set up the configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'malaria_dashboard.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Import and register the Blueprint from routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create the database tables
    with app.app_context():
        db.create_all()

    return app
