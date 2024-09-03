from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
import datetime


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), unique=True)
    director: Mapped[str] = mapped_column(String(64))
    release_date: Mapped[datetime.date] = mapped_column(Date)
    duration: Mapped[int] = mapped_column()  # in minutes
    genre: Mapped[str] = mapped_column(String(32))
    rating: Mapped[float] = mapped_column()

    def __repr__(self):
        return f'Movie({self.id}, "{self.title}")'
