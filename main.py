from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movie_list = {
    "1": "The Shawshank Redemption",
    "2": "The Godfather",
    "3": "The Godfather: Part II",
    "4": "The Dark Knight",
    "5": "12 Angry Men",
}


class Movie(BaseModel):
    movie_name: str
    movie_rank: int
    movie_genre: str
    movie_language: Optional[str] = None
    movie_year: Optional[str] = None


@app.get("/movies")
def read_root():
    return movie_list


@app.get("/movies/{rank}")
def read_items(rank: str, q: Optional[str] = None):
    if rank not in movie_list:
        return {"msg": "requested movie data not found"}
    return {"rank": rank, "movie": movie_list[rank]}


@app.post("/movie")
def add_movie(movie: Movie):
    print(type(movie))
    movie_data = movie.dict()
    print(type(movie_data))
    if movie_data["movie_rank"] > 9:
        return {"message": "Good Movie"}
    else:
        return {"message": "Average Movie", **movie_data}
