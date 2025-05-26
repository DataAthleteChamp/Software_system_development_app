from fastapi import APIRouter, Form
from jose import jwt
from datetime import timedelta

router = APIRouter()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

@router.post("/token")
def login(email: str = Form(...), password: str = Form(...)):
    # Fake check
    if email == "doctor@example.com" and password == "1234":
        access_token_expires = timedelta(minutes=30)
        access_token = jwt.encode({"sub": email}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": access_token, "token_type": "bearer"}
    raise Exception("Invalid credentials")