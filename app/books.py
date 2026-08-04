from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int

books = []
@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books")
def get_books():
    return books

@app.get("/books/{index}")
def get_book(index: int):
    if index < len(books):
        return books[index]
    return {"error": "Book not found"}

@app.put("/books/{index}")
def update_book(index: int, new_book: Book):
    if index < len(books):
        books[index] = new_book
        return new_book
    return {"error": "Book not found"}

@app.delete("/books/{index}")
def delete_book(index: int):
    if index < len(books):
        return books.pop(index)
    return {"error": "Book not found"}
