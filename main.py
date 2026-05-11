from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


users_db = {}


class UserRegister(BaseModel):
    username: str
    password: str

# Register API
@app.post("/register")
def register(user: UserRegister):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    
    users_db[user.username] = user.password
    
    return {
        "message": "User meera"
        " registered successfully",
        "username": user.username
    }
