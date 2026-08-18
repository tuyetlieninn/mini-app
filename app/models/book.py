from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.db.database import Base

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    year: Mapped[int]
    summary: Mapped[str | None]

    author_id: Mapped[int | None] = mapped_column(ForeignKey("authors.id"))
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))

    author: Mapped["Author"] = relationship("Author", back_populates="books")
    category: Mapped["Category"] = relationship("Category", back_populates="books")
