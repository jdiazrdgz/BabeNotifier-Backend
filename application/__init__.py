from flask import Flask
from unipath import Path
from .config.DevelopmentConfig import DevelopmentConfig
from .config.ProductionConfig import ProductionConfig
from pusher import Pusher
from google.oauth2 import service_account
from google.cloud import firestore


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
    auth_file_folder = Path(__file__).ancestor(1)
    auth_file_name = '/babenotifier-b3a726e28ca9.json'

    print(str(auth_file_folder)+auth_file_name)
    credentials = service_account.Credentials.from_service_account_file(
        str(auth_file_folder)+auth_file_name)

    fire_store = firestore.Client(credentials=credentials, project='babenotifier')

    with app.app_context():
        from .routes import routes
        return app
