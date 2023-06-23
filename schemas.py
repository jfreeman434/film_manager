from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    login: str
    age: int
    admin: bool


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Director(BaseModel):
    id: int
    name: str
    date_of_birth: str

    class Config:
        orm_mode = True


class Film(BaseModel):
    id: int
    name: str
    genre: str
    director_id: List[Director] = []
    rate: float
    year: int
    minutes: int

    class Config:
        orm_mode = True


class Favourites(BaseModel):
    user_id: int
    film_id: int

    class Config:
        orm_mode = True


class Wishlist(BaseModel):
    user_id: int
    film_id: int

    class Config:
        orm_mode = True
