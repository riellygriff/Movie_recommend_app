from imdb import IMDb
import pandas as pd

def get_movie_data(id):
    """
    This function takes in a movie id from the IMDb api and pulls data for that movie such as the name,director,genre
    year it was released, and the main cast
    :param id: int
    :return: dataframe
    """
    ia = IMDb()
    movie=ia.get_movie(id)
    cast = [movie['cast'][0]['name'], movie['cast'][1]['name'], movie['cast'][2]['name'], movie['cast'][3]['name'],
            movie['cast'][4]['name']]
    data = pd.DataFrame([id, movie['title'], movie['year'], movie['director'][0]['name'], movie['genre'], cast])
    data = data.transpose()
    data.columns = ['MovieID', 'Title', 'Year', 'Director', 'Genres', 'Main Cast']
    data.set_index('MovieID', inplace=True)
    return data


def top_250():
    """
    This function takes the top 250 movies off of IMDb and put the movie along with its data into a dataframe and
    saves the dataframe as a csv file
    :return: DataFrame
    """
    ia = IMDb()
    movies = ia.get_top250_movies()

    ids = [movie.movieID for movie in movies]

    for i in range(len(ids)):
        if ids[i] == ids[0]:
            df=get_movie_data(ids[i])
        else:
            df = df.append(get_movie_data(ids[i]))
    df.to_csv(r'Movie_Data.csv')
    return df


#top_250()
