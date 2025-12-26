from uuid import UUID, uuid4
from datetime import datetime
from firebase import db

USERS = "users"
AUTHORS = "authors"
BOOKS = "books"


def convert_uuid_to_str(data: dict):
    for k, v in data.items():
        if isinstance(v, UUID):
            data[k] = str(v)
    return data


def create_doc(collection: str, data: dict):
    data = convert_uuid_to_str(data)

    doc_id = str(data.get("id") or uuid4())
    data["id"] = doc_id
    data["created_at"] = datetime.utcnow().isoformat()
    data["updated_at"] = datetime.utcnow().isoformat()

    db.collection(collection).document(doc_id).set(data)
    return data


def get_doc_by_id(collection: str, doc_id: str):
    doc = db.collection(collection).document(str(doc_id)).get()
    return doc.to_dict() if doc.exists else None


def get_all_docs(collection: str):
    return [doc.to_dict() for doc in db.collection(collection).stream()]


def update_doc(collection: str, doc_id: str, data: dict):
    data = convert_uuid_to_str(data)
    ref = db.collection(collection).document(str(doc_id))

    if not ref.get().exists or not data:
        return None

    data["updated_at"] = datetime.utcnow().isoformat()
    ref.update(data)
    return ref.get().to_dict()


def delete_doc(collection: str, doc_id: str):
    ref = db.collection(collection).document(str(doc_id))
    if not ref.get().exists:
        return False
    ref.delete()
    return True


def get_user_full_data(user_id: str):
    user_id = str(user_id)

    authors = []
    authors_query = db.collection(AUTHORS).where("user_id", "==", user_id).stream()

    for a in authors_query:
        author = a.to_dict()
        author_id = author.get("id")

        books = [
            b.to_dict()
            for b in db.collection(BOOKS)
            .where("author_id", "==", author_id)
            .stream()
        ]

        author["books"] = books
        authors.append(author)

    user_books = [
        b.to_dict()
        for b in db.collection(BOOKS)
        .where("user_id", "==", user_id)
        .stream()
    ]

    return {
        "user_id": user_id,
        "total_authors": len(authors),
        "total_books": len(user_books),
        "authors": authors,
        "user_books": user_books,
    }


def get_books_by_user(user_id: str):
    return [
        b.to_dict()
        for b in db.collection(BOOKS)
        .where("user_id", "==", str(user_id))
        .stream()
    ]


def get_books_by_author(author_id: str):
    return [
        b.to_dict()
        for b in db.collection(BOOKS)
        .where("author_id", "==", str(author_id))
        .stream()
    ]
