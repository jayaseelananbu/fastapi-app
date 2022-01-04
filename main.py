from typing import Optional
from fastapi import FastAPI

app = FastAPI()

movie_list = {
    "1": "The Shawshank Redemption",
    "2": "The Godfather",
    "3": "The Godfather: Part II",
    "4": "The Dark Knight",
    "5": "12 Angry Men",
}


@app.get("/movies")
def read_root():
    return movie_list


@app.get("/movies/{rank}")
def read_items(rank: str, q: Optional[str] = None):
    if rank not in movie_list:
        return {"msg": "requested movie data not found"}
    return {"rank": rank, "movie": movie_list[rank]}

