from flask_restful import Resource
from application.config.FirestoreConfig import get_connection

db = get_connection()


class Users(Resource):
    # List all users in Users collection

    def get(self):
        users = db.collection(u'users').stream()
        for user in users:
            print(user.to_dict())

        """return {
            "success": True,
            "message": "Users",
            "data": [x.json() for x in users]
        }, 200"""
