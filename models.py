from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Float,
    Integer,
    String
)

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    admin = Column(Boolean, default=False)


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(Date)


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    genre = Column(String)
    rate = Column(Float)
    year = Column(Integer)
    minutes = Column(Integer)
    director_id = Column(Integer, ForeignKey("directors.id"))


class Favourites(Base):
    __tablename__ = "favourites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    film_id = Column(Integer, ForeignKey("films.id"))


class WishList(Base):
    __tablename__ = "whishlist"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    film_id = Column(Integer, ForeignKey("films.id"))
