from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
CORS(app)

# Assuming the CSV file is in the same directory as the script
CSV_FILE_PATH = 'imdb_top_1000.csv'

# @app.route('/random-movies')
# def random_movies():
#     movies_dict = {}
#     df = pd.read_csv(CSV_FILE_PATH)
#     random_movies = df.sample(5).to_dict(orient='records')
#     for i in range(5):
#         movies_dict[i] = random_movies[i]['Series_Title'], random_movies[i]['id'], random_movies[i]['Poster_Link']
#     return jsonify(movies_dict)

@app.route('/random-movies')
@cross_origin()
def random_movies():
    df = pd.read_csv(CSV_FILE_PATH)
    df = df.where(pd.notnull(df), None) 
    random_movies = df.sample(5).to_dict(orient='records')
    return jsonify(random_movies)


if __name__ == '__main__':
    app.run(debug=True)
