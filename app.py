import streamlit as st
import pickle
import pandas as pd
import os
import gdown
import requests


similarity = None
movies = None

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
    
def recommend(movie):
    global similarity, movies

    if similarity is None:
        movies, similarity = load_data()

    movie_idx = movies[movies['title']== movie].index[0]
    similarity_array = similarity[movie_idx]


    movies_list = sorted(list(enumerate(similarity_array)),reverse=True,key=lambda x:x[1])[1:6]
    # sorted the similarity_array of the particular movie in decending order on the basis of score and made tupple of i9ndex and score to identify the movie

    recommended_movies =[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        #fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster

@st.cache_resource
def load_data():
    if not os.path.exists(SIMILARITY_FILE):
        with st.spinner("Downloading similarity model..."):
            gdown.download(SIMILARITY_URL, SIMILARITY_FILE, quiet=False, fuzzy=True)


    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    similarity = pickle.load(open(SIMILARITY_FILE, "rb"))

    return pd.DataFrame(movies_dict), similarity


movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

SIMILARITY_FILE = "similarity.pkl"
SIMILARITY_URL = "https://drive.google.com/file/d/1MHYUMaeXQWdWx7YxUtA3V_B0dGlqxaHO/view?usp=sharing"


st.title("Movie Recommendation System")

selected_movie_name= st.selectbox("Select the movie that you like, and I will recommend similar movies",movies['title'].values)

col_btn1, col_btn2, col_btn3, col_btn4, col_btn5, col_btn6, col_btn7 = st.columns([1, 1, 1, 1,5 ,1,1,1])

with col_btn4:
    recommend_clicked = st.button("Recommend")

if recommend_clicked:
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.caption(names[0])
    with col2:
        st.image(posters[1])
        st.caption(names[1])
    with col3:
        st.image(posters[2])
        st.caption(names[2])
    with col4:
        st.image(posters[3])
        st.caption(names[3])
    with col5:
        st.image(posters[4])
        st.caption(names[4])












