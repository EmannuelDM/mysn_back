from auth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from .schemas import PostBase, PostDisplay
from db.database import get_db
from .services import db_create, db_get_all, db_delete
from typing import List
import random
import string
import shutil
from users.schemas import UserBase


router = APIRouter(
  prefix='/post',
  tags=['post']
)

image_url_types = ['absolute', 'relative']

@router.post('', response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  if not request.image_url_type in image_url_types:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
              detail="Parameter image_url_type can only take values 'absolute' or 'relative'.")
  return db_create(db, request)

@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
  return db_get_all(db)

@router.post('/image')
def upload_image(image: UploadFile = File(...), current_user: UserBase = Depends(get_current_user)):
  letters = string.ascii_letters
  rand_str = ''.join(random.choice(letters) for i in range(6))
  new = f'_{rand_str}.'
  filename = new.join(image.filename.rsplit('.', 1))
  path = f'images/{filename}'

  with open(path, "w+b") as buffer:
    shutil.copyfileobj(image.file, buffer)
  
  return {'filename': path}

@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return db_delete(db, id, current_user.id)