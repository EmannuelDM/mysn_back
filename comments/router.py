from .schemas import CommentBase
from users.schemas import UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from .services import db_get_all,db_create
from auth.oauth2 import get_current_user

router = APIRouter(
  prefix='/comment',
  tags=['comment']
)

@router.get('/all/{post_id}')
def comments(post_id: int, db: Session = Depends(get_db)):
  return db_get_all(db, post_id)


@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return db_create(db, request)