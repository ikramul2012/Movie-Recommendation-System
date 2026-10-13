import streamlit as st
import pickle
import pandas as pd 
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a2c5dda8ae5953dbabc354bedd368757&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#we select 1 movie it will return 5
def recommend(movie):
    #for index position
    #movie_index = new_df[new_df['title']==movie].index[0]
    #in orginal data set data frame is new_df
    # but here data frame is movies 
    movie_index = movies[movies['title']==movie].index[0]
    #distance
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        #movie id will track which movie is this 
        movie_id = movies.iloc[i[0]].movie_id
  
        recommended_movies.append(movies.iloc[i[0]].title)
              #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id)) 
    return recommended_movies,recommended_movies_posters

#full code of movies which is converted into dictionary
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
#all movie title stored into pandas data frame
movies = pd.DataFrame(movies_dict) 

similarity = pickle.load(open('similarity.pkl','rb'))


#title of web page
st.title('Movie Rocomender System')

#adding text box for users to type
selected_movie_name = st.selectbox(
'Enter movie name',
#text box where we have 5000 titles to choose
movies['title'].values
)

#adding button
if st.button('Recommend'):
    #after button press it will return 5 movies
    names,posters = recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])        
    