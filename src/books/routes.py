from fastapi import APIRouter, HTTPException

book_router = APIRouter()

@book_router.get("/")
def get_books():
    return {"message": "Hello World"}

@book_router.get("/exception")
def raise_exception():
    raise Exception("This is a test exception")
