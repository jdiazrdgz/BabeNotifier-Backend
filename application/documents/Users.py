from application.config.FirestoreConfig import get_connection
db = get_connection()


def get_user_by_email(email):
    users_references = db.collection('users').where("email", "==", email).stream()
    users_documents = [document.to_dict() for document in users_references]
    if len(users_documents) > 0:
        return users_documents[0]
    else:
        return None


def create_user(name, email, password):
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    user_reference = db.collection('users').add(user)
    return user_reference
