from fastapi import FastAPI
import Movie_Clusters
import uvicorn
from imdb import IMDb

ia=IMDb()
app = FastAPI()

@app.get('/movie_id/')
def get_movie_id(movie_name: str):
    movie = ia.search_movie(movie_name)[0]
    movie_id = movie.movieID
    return {'movie_id': movie_id}


@app.get('/recommendations/')
def get_recs(movie_id: str):
    df= Movie_Clusters.get_cluster(movie_id)
    return {'recommendations' : df.to_dict()}


# if __name__ == '__main__':
#     uvicorn.run("api:app", host="127.0.0.1", port=5000)