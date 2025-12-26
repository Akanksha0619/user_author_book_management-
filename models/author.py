from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class AuthorCreate(BaseModel):
    authorname: str
    country: str
    status: Optional[str] = "active"
    user_id: UUID


class AuthorUpdate(BaseModel):
    authorname: str | None = None
    country: str | None = None
    status: str | None = None

    class Config:
        json_schema_extra = {"example": {}}
