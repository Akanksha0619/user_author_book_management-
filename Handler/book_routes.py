from fastapi import APIRouter, HTTPException
from models.book import BookCreate, BookUpdate
from unit.book import (
    create_book,
    get_all_books,
    get_book_by_id,
    update_book_by_id,
    delete_book_by_id,
    user_full_data,
    books_by_user,
    books_by_author
)

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/")
def add_book(book: BookCreate):
    return create_book(book.model_dump())

@router.get("/")
def list_books():
    return get_all_books()

@router.get("/{book_id}")
def view_book(book_id: str):
    book = get_book_by_id(book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book

@router.patch("/{book_id}")
def edit_book(book_id: str, updated: BookUpdate):
    data = updated.model_dump(exclude_unset=True)
    return update_book_by_id(book_id, data)

@router.delete("/{book_id}")
def remove_book(book_id: str):
    if not delete_book_by_id(book_id):
        raise HTTPException(404, "Book not found")
    return {"message": "Book deleted successfully"}

@router.get("/user/{user_id}/full")
def full_user_data(user_id: str):
    return user_full_data(user_id)

@router.get("/user/{user_id}")
def user_books(user_id: str):
    return books_by_user(user_id)

@router.get("/author/{author_id}")
def author_books(author_id: str):
    return books_by_author(author_id)
