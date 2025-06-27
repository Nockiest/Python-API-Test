from flask import Flask
from .routes import bp  # Import the blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_SETTINGS', silent=True)

    app.register_blueprint(bp)  # Register the blueprint

    return app