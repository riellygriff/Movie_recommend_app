import pandas as pd
import streamlit as st
import requests


st.title('Movie Recommendations')
movie_name = st.text_input('Enter a Movie that you would like recommendations similar to:')
movie_id = requests.get(f'http://backend:8000/movie_id/?movie_name={movie_name}').json()
recommendations = requests.get(f'http://backend:8000/recommendations/?movie_id={movie_id["movie_id"]}').json()
df = pd.DataFrame.from_dict(recommendations['recommendations'])

st.dataframe(df)




