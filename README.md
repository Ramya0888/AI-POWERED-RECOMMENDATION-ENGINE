COMPANY: CODTECH IT SOLUTIONS

NAME:RAMYA.S

INTERN ID:CT12QTC

DOMAIN:BACK END DEVELOPMENT

DURATION:8 WEEKS

MENTOR:NEELA SANTOSH

# AI-Powered Movie Recommendation Engine

## Introduction:
In the digital age, personalized content recommendations have become essential in enhancing user experience. This project, **AI-Powered Movie Recommendation Engine**, aims to provide users with movie suggestions based on their preferences and past interactions. By leveraging **Machine Learning (ML)** techniques and **FastAPI**, this system delivers fast, efficient, and accurate recommendations.

## Project Overview
The **AI-Powered Movie Recommendation Engine** is built using **FastAPI** for the backend, **Pandas** and **Scikit-Learn** for data processing, and a small dataset of movie ratings. The system implements a **collaborative filtering** approach using **cosine similarity** to find movies that users might like based on their historical ratings.

## Features
- **User-Based Collaborative Filtering**: Uses past ratings from similar users to suggest movies.
- **REST API with FastAPI**: A lightweight and high-performance API to serve recommendations.
- **Efficient Data Handling**: Uses a compact dataset to avoid memory issues and improve processing speed.
- **Modular Codebase**: Well-structured Python scripts for data handling, recommendation generation, and API deployment.

## Tech Stack
- **Backend Framework**: FastAPI
- **Machine Learning Libraries**: Scikit-Learn, Pandas, NumPy
- **Data Storage**: CSV files (ratings and movies dataset)
- **Deployment**: Docker (optional for containerized deployment)

## System Architecture
The recommendation engine follows a simple architecture:
1. **Data Preprocessing**: Load and clean datasets containing movie information and user ratings.
2. **User-Movie Matrix Generation**: Create a pivot table where rows represent users and columns represent movies, with values as ratings.
3. **Similarity Computation**: Compute user-to-user similarity using **cosine similarity**.
4. **Recommendation Generation**: Based on similar users, recommend movies that the user has not yet watched.
5. **API Integration**: Serve recommendations via FastAPI.

## Dataset
This project uses a **small-sized dataset** to ensure efficient computations while maintaining accuracy. The dataset contains:
- **Movies Data (`movies_small.csv`)**: Contains `movieId`, `title`, and `genre`.
- **Ratings Data (`ratings_small.csv`)**: Contains `userId`, `movieId`, and `rating`.

## Implementation Details
### **Recommendation Algorithm**
The **collaborative filtering approach** is used, where:
- A user-movie matrix is built with ratings.
- The **cosine similarity** between users is computed.
- The system finds users with the highest similarity to the target user.
- Based on these similar users' ratings, the system recommends movies that the target user has not yet watched.

### **API Implementation**
The FastAPI-based backend allows users to get recommendations via an API call:
```python
from fastapi import FastAPI
from recommendation import recommend_movies

app = FastAPI()

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    recommendations = recommend_movies(user_id)
    return {"user_id": user_id, "recommendations": recommendations}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
### **Recommendation Function**
```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies_small.csv")
ratings = pd.read_csv("ratings_small.csv")

data = pd.merge(ratings, movies, on="movieId")
user_movie_ratings = data.pivot_table(index="userId", columns="title", values="rating").fillna(0)

similarity_matrix = cosine_similarity(user_movie_ratings)

def recommend_movies(user_id, top_n=3):
    if user_id not in user_movie_ratings.index:
        return ["User not found."]
    
    user_idx = user_movie_ratings.index.get_loc(user_id)
    similar_users = similarity_matrix[user_idx]
    top_users = similar_users.argsort()[::-1][1:top_n+1]

    recommended_movies = set()
    for similar_user in top_users:
        watched_movies = user_movie_ratings.iloc[similar_user].dropna().index
        recommended_movies.update(watched_movies)

    return list(recommended_movies)[:top_n]
```

## Deployment
To deploy the recommendation engine using **Docker**, create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
Then, build and run the Docker container:
```sh
docker build -t movie-recommendation .
docker run -p 8000:8000 movie-recommendation
```

## Conclusion
This **AI-Powered Movie Recommendation Engine** efficiently provides personalized movie recommendations based on user preferences. Using **collaborative filtering** and **FastAPI**, it ensures scalability, speed, and accuracy. This project can be extended further by integrating a **content-based filtering** approach, adding a **database** for persistent storage, or deploying it on a cloud platform for real-world use.This project is a solid foundation for recommendation systems and can be enhanced with more advanced ML techniques for better personalization.

## OUTPUT:

## MOVIE RECOMMENDATION FOR USER ID 1:
## MOVIE RECOMMENDATION FOR USER ID 20:
## MOVIE RECOMMENDATION FOR USER ID 23:





