from fastapi import APIRouter, HTTPException
from models.author import AuthorCreate, AuthorUpdate
from unit.author import (
    create_author,
    get_all_authors,
    get_author_by_id,
    update_author_by_id,
    delete_author_by_id
)

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/")
def add_author(author: AuthorCreate):
    try:
        return create_author(author.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
def list_authors():
    return get_all_authors()

@router.get("/{author_id}")
def view_author(author_id: str):
    author = get_author_by_id(author_id)
    if not author:
        raise HTTPException(404, "Author not found")
    return author

@router.patch("/{author_id}")
def edit_author(author_id: str, updated: AuthorUpdate):
    data = updated.model_dump(exclude_unset=True)
    return update_author_by_id(author_id, data)

@router.delete("/{author_id}")
def remove_author(author_id: str):
    if not delete_author_by_id(author_id):
        raise HTTPException(404, "Author not found")
    return {"message": "Author deleted successfully"}
