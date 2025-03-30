from fastapi import FastAPI
from recommendation import recommend_movies

app = FastAPI()

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    recommendations = recommend_movies(user_id)
    
    if isinstance(recommendations, list) and "User not found." in recommendations:
        return {"error": "User not found."}
    
    response = [{"movie_title": title} for title in recommendations]
    return {"user_id": user_id, "recommendations": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
