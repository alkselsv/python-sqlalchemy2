from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base
import datetime


class Director(Base):
    __tablename__ = "directors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True)

    movies: Mapped[list["Movie"]] = relationship("Movie", back_populates="director")

    def __repr__(self):
        return f'Director({self.id}, "{self.name}")'


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), unique=True)
    director_id: Mapped[int] = mapped_column(ForeignKey("directors.id"), index=True)
    release_date: Mapped[datetime.date] = mapped_column(Date)
    duration: Mapped[int] = mapped_column()  # in minutes
    genre: Mapped[str] = mapped_column(String(32))
    rating: Mapped[float] = mapped_column()

    director: Mapped[Director] = relationship("Director", back_populates="movies")

    def __repr__(self):
        return f'Movie({self.id}, "{self.title}")'
