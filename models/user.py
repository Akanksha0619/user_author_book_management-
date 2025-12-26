from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone: str
    gender: Literal["Male", "Female", "Othe"]
    status: Optional[str] = "active"
    role: Optional[str] = "user"


class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    gender: str | None = None
    status: str | None = None
    role: str | None = None

    class Config:
        json_schema_extra = {"example": {}}
