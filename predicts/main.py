import requests
import csv
import os

# Replace 'YOUR_API_KEY' with your actual API key (if required by the API)
API_KEY = 'e35c7f6c'
BASE_URL = 'http://www.omdbapi.com/'

def get_movie_data(title):
    params = {'apikey': API_KEY, 't': title}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def create_dataset(movie_titles):
    dataset = []

    for title in movie_titles:
        movie_data = get_movie_data(title)

        if movie_data.get('Response') == 'True':
            dataset.append({
                'Title': movie_data.get('Title', ''),
                'Year': movie_data.get('Year', ''),
                'Genre': movie_data.get('Genre', ''),
                'Director': movie_data.get('Director', ''),
                'imdbRating': movie_data.get('imdbRating', '')
            })
        else:
            print(f"Failed to fetch data for '{title}': {movie_data.get('Error', 'Unknown error')}")

    return dataset

def save_to_csv(dataset, filename='movie_dataset.csv'):
    fields = ['Title', 'Year', 'Genre', 'Director', 'imdbRating']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        
        # Write the header
        csvwriter.writeheader()

        # Write the data
        csvwriter.writerows(dataset)

if __name__ == '__main__':
    # Replace 'Your_Movie_Titles' with a list of movie titles you want to fetch
    movie_titles = ['Inception', 'The Dark Knight', 'The Shawshank Redemption', 'Pulp Fiction']
    
    movie_dataset = create_dataset(movie_titles)
    
    if movie_dataset:
        save_to_csv(movie_dataset)
        print("Dataset created and saved to 'movie_dataset.csv'")
    else:
        print("No valid movie data to save.")
