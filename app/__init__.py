from flask import Flask
from .routes import main  # Import the 'main' blueprint

def create_app():
    app = Flask(__name__)

    # Register the blueprint with the app
    app.register_blueprint(main)

    return app
