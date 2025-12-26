from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserUpdate
from unit.user import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user_by_id,
    delete_user_by_id
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def add_user(user: UserCreate):
    return create_user(user.model_dump())

@router.get("/")
def list_users():
    return get_all_users()

@router.get("/{user_id}")
def view_user(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user

@router.patch("/{user_id}")
def edit_user(user_id: str, updated: UserUpdate):
    data = updated.model_dump(exclude_unset=True)
    return update_user_by_id(user_id, data)

@router.delete("/{user_id}")
def remove_user(user_id: str):
    if not delete_user_by_id(user_id):
        raise HTTPException(404, "User not found")
    return {"message": "User deleted successfully"}
