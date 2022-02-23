import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import Movie_Data


def get_cluster(movie_id):
    """
    This function takes in a movie id from the IMdb website and puts it into a cluster of similar movies from the movie
    data csv file. It then returns a dataframe of the movie names and year released of the movies that are similar to
    the movie id input
    :param movie_id:
    :return: dataframe
    """
    # reading in the csv with the top 250 movies on IMDb
    df = pd.read_csv('Movie_Data.csv')
    df.set_index('MovieID', inplace=True)

    # getting the movie data for the movie id input and adding it to the top 250 movies
    data = Movie_Data.get_movie_data(movie_id)
    df = df.append(data)
    df.iloc[-1, -2] = str(df.iloc[-1, -2])
    df.iloc[-1, -1] = str(df.iloc[-1, -1])

    # converting the features into a data type that can be read by the model
    train = []
    vec = TfidfVectorizer()
    features = ['Title', 'Director', 'Genres', 'Main Cast']
    for i in range(len(features)):
        feat = vec.fit_transform(df[features[i]])
        train.append(pd.DataFrame(feat.toarray(), columns=sorted(vec.vocabulary_.keys())))

    # normalizing the data on the year a movie was released
    feature = pd.concat([train[0], train[1], train[2], train[3]], axis=1)
    feature['year'] = df['Year'].reset_index()['Year']
    feature['year'] = (feature['year'] - feature['year'].min()) / (feature['year'].max() - feature['year'].min())

    # split data back into top 250 and the movie from the input
    train = feature[:-1]
    prediction = feature[-1:]

    # use a kmeans model to find the cluster that is associated with the given movie
    model = KMeans(n_clusters=15, random_state=0)
    model.fit(train)
    group = model.predict(prediction)
    grouping = df.iloc[:-1].iloc[model.labels_ == group]

    return grouping[['Title', 'Year']]
