import streamlit as st
import pickle
import pandas as pd

movie_dict=pickle.load(open("movie_dict.pkl",'rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open("similarity.pkl",'rb'))
st.title("Movie Recommendor ")

def recommend(movie):
  recommended_movies=[]
  index=movies[movies['title']==movie].index[0]
  distances=sorted(enumerate(similarity[index]), reverse=True, key=lambda x:x[1])
  for i in distances[1:6]:
    recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies

option=st.selectbox("Type or select a movie:",
             movies['title'].values
)

if st.button("Recommend"):
    st.write("Recommendations:")
    recomendations=recommend(option)
    for i in recomendations:
       st.write(i)