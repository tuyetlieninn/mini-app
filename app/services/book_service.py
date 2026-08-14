from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from fastapi import HTTPException

from app.models import Book, Author
from app.schemas.book import BookRead, BookCreate, BookUpdate


def to_book_read(book: Book) -> BookRead:
    return BookRead(
        id=book.id,
        title=book.title,
        year=book.year,
        summary=book.summary,
        author_id = book.author_id,
        author_name = book.author.name if book.author else None,
)
def _ensure_author_exists(db: Session, author_id: int | None) -> None:
    if author_id is None:
        return
    if db.get(Author, author_id) is None:
        raise HTTPException(status_code=404, detail="Author not found")

def list_books(db: Session) -> list[BookRead]:
    stmt = select(Book).options(joinedload(Book.author)).order_by(Book.id)
    return [to_book_read(b) for b in db.scalars(stmt)]

def get_book(db: Session, book_id: int) -> BookRead:
    stmt = select(Book).options(joinedload(Book.author)).where(Book.id == book_id)
    book = db.scalars(stmt).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return to_book_read(book)

def create_book(db: Session, payload: BookCreate) -> BookRead:
    _ensure_author_exists(db, payload.author_id)
    book = Book(**payload.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return get_book(db, book.id)

def update_book(db: Session, book_id: int, payload: BookUpdate) -> BookRead:
    book = db.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    _ensure_author_exists(db, payload.author_id)

    for field, value in payload.model_dump().items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return get_book(db, book.id)

def delete_book(db: Session, book_id: int) -> None:
    book = db.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()

