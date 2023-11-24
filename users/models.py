import datetime
from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship



class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    last_name = Column(String)
    sex_type = Column(String)
    birth_date = Column(DateTime)
    items = relationship('DbPost', back_populates='user')
    created_at = Column(DateTime, default=datetime.datetime.now())
