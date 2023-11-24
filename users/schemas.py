from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    name: str
    last_name: str
    sex_type: str
    birth_date: datetime


class UserUpdate(BaseModel):
    username: str
    email: str
    name: str
    last_name: str
    sex_type: str
    birth_date: datetime


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    name: str
    last_name: str
    sex_type: str
    birth_date: datetime

    class Config:
        from_attributes = True


# For PostDisplay
class User(BaseModel):
  username: str
  class Config():
    from_attributes = True
