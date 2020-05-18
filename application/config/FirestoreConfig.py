from unipath import Path
from google.oauth2 import service_account
from google.cloud import firestore

_db = None


def get_connection():
    global _db
    if not _db:
        auth_file_folder = Path(__file__).ancestor(1)
        auth_file_name = '/babenotifier-bcd20b44be05.json'
        credentials = service_account.Credentials.from_service_account_file(str(auth_file_folder) + auth_file_name)
        _db = firestore.Client(credentials=credentials, project='babenotifier')

    return _db


# List of stuff accessible to importers of this module. Just in case
__all__ = ['get_connection']
