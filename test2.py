import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()

def get_famous_movies():
    famous_movies = set()

    # Fetch the top 250 movies
    try:
        top_250 = ia.get_top250_movies()
        for movie in top_250:
            famous_movies.add(movie['title'])
    except Exception as e:
        print(f"Error fetching top 250 movies: {e}")

    return list(famous_movies)

if __name__ == '__main__':
    famous_movie_titles = get_famous_movies()
    print(f"Total famous movies fetched: {len(famous_movie_titles)}")
    for title in famous_movie_titles[:50]:  # Print the first 50 titles
        print(title)
