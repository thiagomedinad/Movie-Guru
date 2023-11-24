from flask import Flask, jsonify, request
import pandas as pd
from recommender import MovieRecommender

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your DataFrame just once when the server starts
df = pd.read_csv('/home/thiagomedinad/vscode/p-movie/predicts/top_movies.csv')
recommender = MovieRecommender(df)
recommender.vectorize()
recommender.calculate_similarity()
recommender.build_indices()

# Define a route to get movie recommendations
@app.route('/recommend', methods=['GET'])
def get_recommendations():
    # Get movie title from the query string
    title = request.args.get('title', default='', type=str)
    
    # Get number of recommendations from the query string, default is 10
    num_recommendations = request.args.get('num', default=10, type=int)
    
    if title:
        try:
            # Use the recommender to get recommendations
            recommendations = recommender.recommend(title, num_recommendations)
            return jsonify({'recommendation': recommendations})
        except KeyError:
            # If the title does not exist in the dataset
            return jsonify({'error': 'Movie title not found in the dataset'}), 404
    else:
        # If no title is provided in the query string
        return jsonify({'error': 'No movie title provided'}), 400

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True)