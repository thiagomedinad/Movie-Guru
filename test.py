import requests
from bs4 import BeautifulSoup
import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()

def get_movie_names():
    movie_names = []

    top_250 = ia.get_top250_movies()
    print(top_250)

    return movie_names

if __name__ == '__main__':
    ia = imdb.IMDb()
    top = ia.get_top250_movies()
    for i in top:
        print(top['title'])

    # movie_names = get_movie_names()

    # if movie_names:
    #     # print("Movie Names:")
    #     # for name in movie_names:
    #     #     print(name)
    #     print(len(movie_names))
    # else:
    #     print("No movie names to display.")