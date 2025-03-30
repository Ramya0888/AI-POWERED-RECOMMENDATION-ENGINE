import pandas as pd

# Load the full dataset
ratings = pd.read_csv("ml-32m/ratings.csv")

# Step 1: Keep only users who have rated at least 10 movies
user_counts = ratings["userId"].value_counts()
active_users = user_counts[user_counts >= 10].index
ratings = ratings[ratings["userId"].isin(active_users)]

# Step 2: Keep only movies that have at least 50 ratings
movie_counts = ratings["movieId"].value_counts()
popular_movies = movie_counts[movie_counts >= 50].index
ratings = ratings[ratings["movieId"].isin(popular_movies)]

# Step 3: Convert ratings to float32 to save memory
ratings["rating"] = ratings["rating"].astype("float32")

# Step 4: Save the reduced dataset
ratings.to_csv("ratings_small.csv", index=False)

print(f"✅ Reduced dataset saved as ratings_small.csv with {ratings.shape[0]} rows.")
