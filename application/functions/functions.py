def get_firestore_document_with_id(document):
    document_id = document.id
    document_dict = document.to_dict()
    document_dict['id'] = document_id
    return document_dict
