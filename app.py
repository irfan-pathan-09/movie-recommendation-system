import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests

movies = joblib.load('movies.pkl')
movies_list = movies['title'].values
similarity = joblib.load('similarity.pkl')

# def fetch_poster(movie_id):
#     response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
#     response_json = response.json()
#     print(response_json)
#     return "https://image.tmdb.org/t/p/w500" + response_json['poster_path'] # complete poster path


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": "8265bd1679663a7ea12ac168da84d2e8",
        "language": "en-US"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=5,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()   # catches 4xx / 5xx errors
        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return None


def recommender(movie):
    st.write("Here are your top 5 Similar movies")
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        poster = fetch_poster(movies.iloc[i[0]].movie_id)
        recommended_movie.append(movies.iloc[i[0]].title)
        if poster:
            recommended_movie_posters.append(poster)
        else:
            recommended_movie_posters.append("https://via.placeholder.com/300x450?text=No+Image")

    return recommended_movie,recommended_movie_posters

st.title('Movie Recommendation System')


selected_movie = st.selectbox(
    'search for a movie',
    options=movies_list
)

if st.button('recommend movie'):
    names,posters = recommender(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    columns = st.columns(5)

    for i in range(5):
        with columns[i]:
            st.text(names[i])
            st.image(posters[i])

# https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=eng-US
#  api key = 8265bd1679663a7ea12ac168da84d2e8

