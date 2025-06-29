import streamlit as st 
import pickle
import pandas as pd   

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]      # this will find index of the user's movies
    distances = similarity[movie_index]                              # this will find similarity of user's movies to other movies
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]      # enumerate will create all data with its index in tuple format so that after sorting ccorresonding index will not lost
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #ffetch poster forom api
        
        recommended_movies.append(movies.iloc[i[0]].title)    
    return recommended_movies

##IMPORTING DATA AND DISTANCE OF ONE MOVIES TO ANOTHER(cosine_similariity)
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

#title
st.title("🎬 Movie Recommender System 🎬")

#widget box
selected_movies_name = st.selectbox(
    "What's your favourite movie?",
    movies['title'].values
)

#button
if st.button('Recommend'):
    recommendation = recommend(selected_movies_name)
    for i in recommendation:
        st.write(i)                      #write something on hitting
