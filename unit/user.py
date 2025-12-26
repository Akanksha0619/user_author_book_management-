from firestore import create_doc, get_all_docs, get_doc_by_id, update_doc, delete_doc, USERS

def create_user(data: dict):
    return create_doc(USERS, data)

def get_all_users():
    return get_all_docs(USERS)

def get_user_by_id(user_id: str):
    return get_doc_by_id(USERS, user_id)

def update_user_by_id(user_id: str, data: dict):
    return update_doc(USERS, user_id, data)

def delete_user_by_id(user_id: str):
    return delete_doc(USERS, user_id)
