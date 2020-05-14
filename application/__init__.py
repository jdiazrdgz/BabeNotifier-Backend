from flask import Flask
from .config.config import DevelopmentConfig, ProductionConfig
from pusher import Pusher


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # configure pusher object
    pusher = Pusher(
        app_id=app.config["PUSHER_APP_ID"],
        key=app.config["PUSHER_APP_KEY"],
        secret=app.config["PUSHER_APP_SECRET"],
        cluster=app.config["PUSHER_APP_CLUSTER"],
        ssl=app.config["PUSHER_APP_SSL"]
    )

    with app.app_context():
        from .routes import routes
        return app
