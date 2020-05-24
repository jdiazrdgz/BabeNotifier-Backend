from flask_restful import Resource, reqparse
from application.config.FirestoreConfig import get_connection
from application.functions.functions import get_firestore_document_with_id
from application.documents.Users import get_user_by_email, create_user
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

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            "name", type=str, required=True, help="This field cannot be blank."
        )
        parser.add_argument(
            "email", type=str, required=True, help="This field cannot be blank."
        )
        parser.add_argument(
            "password", type=str, required=True, help="This field cannot be blank."
        )

        data = parser.parse_args()
        # Buscar si existe usuario con el correo dado, si es asi decir que ya existe, sino crearlo
        user_document = get_user_by_email(data.email)
        if user_document:
            return {
                "success": False,
                "error-message": "Bad Request",
                "error-description": "The user with that email already exists"
            }, 400
        else:
            user_reference = create_user(name=data.name, email=data.email, password=data.password)
            user_creation_metadata = user_reference[0]
            user_document = user_reference[1].get()
            user = user_document.to_dict()
            print(user)
            return {
                "success": True,
                "message": "User created successfuly",
                "data": json.dumps(user)
            }, 201


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
