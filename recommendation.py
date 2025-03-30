import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("ml-32m/movies_small.csv")
ratings = pd.read_csv("ml-32m/ratings_small.csv")

# Merge ratings with movies
data = pd.merge(ratings, movies, on="movieId")

# Create user-movie ratings matrix
user_movie_ratings = data.pivot_table(index="userId", columns="title", values="rating").fillna(0)

# Compute cosine similarity between users
similarity_matrix = cosine_similarity(user_movie_ratings)

# Function to recommend movies (Ensuring unseen movies are recommended)
def recommend_movies(user_id, top_n=3):
    if user_id not in user_movie_ratings.index:
        return ["User not found."]

    user_idx = user_movie_ratings.index.get_loc(user_id)
    similar_users = similarity_matrix[user_idx]

    # Get similar users, excluding the user itself
    top_users = similar_users.argsort()[::-1][1:top_n+5]  

    user_watched = set(user_movie_ratings.loc[user_id][user_movie_ratings.loc[user_id] > 0].index)
    recommended_movies = {}

    for similar_user in top_users:
        similar_user_movies = user_movie_ratings.iloc[similar_user]
        for movie, rating in similar_user_movies.items():
            if movie not in user_watched and rating > 0:  # Recommend only unseen movies
                if movie not in recommended_movies:
                    recommended_movies[movie] = rating
                else:
                    recommended_movies[movie] += rating  # Sum ratings for better ranking

    # Sort recommended movies by rating and return top_n movies
    recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    return [{"movie_title": movie} for movie, _ in recommended_movies[:top_n]]
