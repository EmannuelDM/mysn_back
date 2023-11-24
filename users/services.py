from fastapi import HTTPException, status
from sqlalchemy import select
from users.models import DbUser
from sqlalchemy.orm.session import Session
from db.hashing import Hash
from users.schemas import UserBase, UserUpdate
from sqlalchemy import select
from fastapi_pagination.ext.sqlalchemy import paginate


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username or request.email,
        email=request.email,
        password=Hash.bcrypt(request.password),
        name=request.name,
        last_name=request.last_name,
        sex_type=request.sex_type,
        birth_date=request.birth_date,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} not found",
        )
    return user


def get_all_users(db: Session, user_filter):
    query = select(DbUser)
    query = user_filter.filter(query)
    query = user_filter.sort(query)
    return paginate(db, query)


def update_user(db: Session, id: int, request: UserUpdate):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.name: request.name,
            DbUser.last_name: request.last_name,
            DbUser.sex_type: request.sex_type,
            DbUser.birth_date: request.birth_date,
        }
    )
    db.commit()
    return {"message": f"User {id} updated."}


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    db.delete(user)
    db.commit()
    return {"message": f"User {id} deleted."}


def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user
