from flask import Flask
from .config.config import DevelopmentConfig, ProductionConfig

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    with app.app_context():
        return app
