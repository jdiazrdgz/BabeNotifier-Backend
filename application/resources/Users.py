from flask_restful import Resource, reqparse
from application.config.FirestoreConfig import get_connection
from application.functions.functions import get_firestore_document_with_id
import json

db = get_connection()


class User(Resource):
    # List all users in Users collection

    def get(self):
        users = db.collection('users').stream()
        users_list = [get_firestore_document_with_id(user) for user in users]

        return {
            "success": True,
            "message": "Users",
            "data": users_list
        }, 200


class UserDetail(Resource):
    # Get user detail by ID

    def get(self, user_id: int):
        if not user_id:
            return {
                "success": False,
                "error-message": "The field user_id is required",
            }, 400

        user_document = db.collection('users').document(user_id).get()
        if not user_document.exists:
            print(user_document, 'odio')
            return {
                "success": True,
                "error-message": "The resource doesn't exist",
            }, 404
        
        user = user_document.to_dict()
        user['id'] = user_document.id
        
        return {
            "success": True,
            "message": "Users",
            "data": user
        }, 200
