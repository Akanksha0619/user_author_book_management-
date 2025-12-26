from firestore import create_doc, get_all_docs, get_doc_by_id, update_doc, delete_doc, USERS, AUTHORS

def create_author(data: dict):
    user_id = str(data.get("user_id"))
    user = get_doc_by_id(USERS, user_id)

    if not user:
        raise ValueError("User not found")

    data["email"] = user.get("email")
    data["user_id"] = user_id

    return create_doc(AUTHORS, data)

def get_all_authors():
    return get_all_docs(AUTHORS)

def get_author_by_id(author_id: str):
    return get_doc_by_id(AUTHORS, author_id)

def update_author_by_id(author_id: str, data: dict):
    return update_doc(AUTHORS, author_id, data)

def delete_author_by_id(author_id: str):
    return delete_doc(AUTHORS, author_id)
