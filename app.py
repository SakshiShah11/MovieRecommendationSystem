import os
import streamlit as st
import pickle
import pandas as pd
import gdown
import requests

# ------------------ PATH SETUP ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIE_DICT_PATH = os.path.join(BASE_DIR, "movie_dict.pkl")
SIMILARITY_FILE = os.path.join(BASE_DIR, "similarity.pkl")

SIMILARITY_URL = "https://drive.google.com/file/d/1MHYUMaeXQWdWx7YxUtA3V_B0dGlqxaHO/view?usp=sharing"

# ------------------ FUNCTIONS ------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=10).json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass
    return "https://via.placeholder.com/300x450?text=No+Image"


def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    similarity_array = similarity[movie_idx]

    movies_list = sorted(
        list(enumerate(similarity_array)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# ------------------ LOAD DATA ------------------
@st.cache_resource
def load_data():
    if not os.path.exists(SIMILARITY_FILE):
        with st.spinner("Downloading similarity model..."):
            gdown.download(SIMILARITY_URL, SIMILARITY_FILE, quiet=False)

    movies_dict = pickle.load(open(MOVIE_DICT_PATH, "rb"))
    similarity = pickle.load(open(SIMILARITY_FILE, "rb"))

    return pd.DataFrame(movies_dict), similarity


movies, similarity = load_data()

# ------------------ UI ------------------
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie you like:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])
