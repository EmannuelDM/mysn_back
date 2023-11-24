from fastapi import HTTPException, status
from .schemas import PostBase
from sqlalchemy.orm.session import Session
from .models import DbPost
import datetime


def db_create(db: Session, request: PostBase):
  new_post = DbPost(
    image_url = request.image_url,
    image_url_type = request.image_url_type,
    caption = request.caption,
    timestamp = datetime.datetime.now(),
    user_id = request.creator_id
  )
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def db_get_all(db: Session):
  return db.query(DbPost).all()

def db_delete(db: Session, id: int, user_id: int):
  post = db.query(DbPost).filter(DbPost.id == id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
          detail=f'Post with id {id} not found')
  if post.user_id != user_id:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
          detail='Only post creator can delete post')

  db.delete(post)
  db.commit()
  return {"message": f"Post {id} deleted."}