import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, data_frame):
        self.df = data_frame
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.indices = None
        self.best_movie = {}

    def vectorize(self):
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.df['combined_features'])

    def calculate_similarity(self):
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def build_indices(self):
        self.indices = pd.Series(self.df.index, index=self.df['Series_Title']).drop_duplicates()

    def recommend(self, title, num_recommendations=10):
        idx = self.indices[title]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        movie_indices = [i[0] for i in sim_scores]
        grades = [i[1] for i in sim_scores]

        self.best_movie[grades[0]] = self.df['Series_Title'].iloc[movie_indices[0]]

        return self.best_movie[grades[0]]