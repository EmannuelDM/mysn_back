from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from db.database import get_db
from users import services
from config import global_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, global_settings.SECRET_KEY, algorithm=global_settings.ALGORITHM)
  return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, global_settings.SECRET_KEY, algorithms=[global_settings.ALGORITHM])
    username: str = payload.get("username")
    if username is None:
      raise credentials_exception
  except JWTError:
    raise credentials_exception
  user = services.get_user_by_username(db, username=username)
  if user is None:
    raise credentials_exception
  return user