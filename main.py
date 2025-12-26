from fastapi import FastAPI
from Handler.user_routes import router as user_router
from Handler.author_routes import router as author_router
from Handler.book_routes import router as book_router

app = FastAPI(title="User-Author-Book CRUD with Firestore")

app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)

@app.get("/")
def home():
    return {"message": "Welcome To Home Page"}
