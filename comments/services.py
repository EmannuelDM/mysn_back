from datetime import datetime
from sqlalchemy.orm import Session
from .models import DbComment
from .schemas import CommentBase


def db_create(db: Session, request: CommentBase):
  new_comment = DbComment(
    text = request.text,
    username = request.username,
    post_id = request.post_id,
    timestamp = datetime.now()
  )
  db.add(new_comment)
  db.commit()
  db.refresh(new_comment)
  return new_comment



def db_get_all(db: Session, post_id: int):
  return db.query(DbComment).filter(DbComment.post_id == post_id).all()