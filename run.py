from app import create_app
"""The module creates the Flask application and runs it."""


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
