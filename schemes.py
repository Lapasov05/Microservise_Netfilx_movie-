from datetime import datetime
from pydantic import BaseModel


class MovieList(BaseModel):
    id: int
    name: str
    description: str
    seen: int
    posted_at: datetime
    like: int
    price: float


class MovieAdd(BaseModel):
    name: str
    description: str
    price: float
    video: str


class AddCategory(BaseModel):
    name: str


class ListCategory(BaseModel):
    id: int
    name: str


class AddCategoryMovie(BaseModel):
    movie_id: int
    category_id: int
