from flask_restful import Resource
from application.config.FirestoreConfig import get_connection
import json

db = get_connection()


class Users(Resource):
    # List all users in Users collection

    def get(self):
        users = db.collection('users').stream()

        return {
            "success": True,
            "message": "Users",
            "data": [eval(json.dumps(user.to_dict())) for user in users]
        }, 200
