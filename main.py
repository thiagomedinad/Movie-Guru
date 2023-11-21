from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

file_path = '/mnt/data/imdb_top_1000.csv'
movies_df = pd.read_csv(file_path)

# Extract the titles from the dataset
movie_titles = movies_df['Series_Title'].tolist()

# Load the dataset just once when the server starts
file_path = 'imdb_top_1000.csv'  # replace with the actual file path
movies_df = pd.read_csv(file_path)

@app.route('/movies', methods=['GET'])
def get_movie_titles():
    # Extract the titles from the dataset
    movie_titles = movies_df['Series_Title'].tolist()
    return jsonify(movie_titles)

if __name__ == '__main__':
    app.run(debug=True)  # Starts the server; make debug=False in a production environment
