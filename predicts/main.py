from flask import Flask, jsonify, request
import pandas as pd
from recommender import MovieRecommender

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

df = pd.read_csv('./top_movies.csv')
recommender = MovieRecommender(df)
recommender.vectorize()
recommender.calculate_similarity()
recommender.build_indices()

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    title = request.args.get('title', default='', type=str)
    
    num_recommendations = request.args.get('num', default=10, type=int)
    
    if title:
        try:
            recommendations = recommender.recommend(title, num_recommendations)
            return jsonify({'recommendation': recommendations})
        except KeyError:
            return jsonify({'error': 'Movie title not found in the dataset'}), 404
    else:
        return jsonify({'error': 'No movie title provided'}), 400

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True)