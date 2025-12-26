from firestore import (
    create_doc,
    get_all_docs,
    get_doc_by_id,
    update_doc,
    delete_doc,
    get_user_full_data,
    get_books_by_user,
    get_books_by_author,
    BOOKS
)

def create_book(data: dict):
    return create_doc(BOOKS, data)

def get_all_books():
    return get_all_docs(BOOKS)

def get_book_by_id(book_id: str):
    return get_doc_by_id(BOOKS, book_id)

def update_book_by_id(book_id: str, data: dict):
    return update_doc(BOOKS, book_id, data)

def delete_book_by_id(book_id: str):
    return delete_doc(BOOKS, book_id)

def user_full_data(user_id: str):
    return get_user_full_data(user_id)

def books_by_user(user_id: str):
    return get_books_by_user(user_id)

def books_by_author(author_id: str):
    return get_books_by_author(author_id)
