from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class DbComment(Base):
  __tablename__ = 'comment'
  id = Column(Integer, primary_key=True, index=True)
  text = Column(String)
  username = Column(String)
  timestamp = Column(DateTime)
  post_id = Column(Integer, ForeignKey('post.id'))
  post = relationship("DbPost", back_populates="comments")