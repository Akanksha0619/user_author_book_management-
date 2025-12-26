from pydantic import BaseModel
from uuid import UUID

class BookCreate(BaseModel):
    title: str
    description: str
    published_year: int
    price: float
    isbn: str
    stock: int
    status: str
    user_id: UUID
    author_id: UUID


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    published_year: int | None = None
    price: float | None = None
    isbn: str | None = None
    stock: int | None = None
    status: str | None = None

    class Config:
        json_schema_extra = {"example": {}}
