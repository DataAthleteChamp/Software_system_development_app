from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid authentication credentials")