from fastapi import FastAPI

app = FastAPI(title="User Service", version="1.0.0")

@app.get("/")
def read_root():
    return {"service": "User Service", "status": "Healthy"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User_{user_id}", "email": f"user{user_id}@example.com"}
