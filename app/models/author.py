from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    bio: Mapped[str | None]
    country: Mapped[str | None]
    birth_year: Mapped[int | None]

    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")
