from typing import Optional
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException
from auth.oauth2 import get_current_user
from db.database import get_db
from users.filters import UserFilter
from users.schemas import UserBase, UserDisplay, UserUpdate
import users.services as services
from fastapi_pagination import Page
from fastapi_filter import FilterDepends

router = APIRouter(prefix="/user", tags=["user"])


# Create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    try:
        return services.create_user(db, request)
    except Exception as e:
        raise Exception(f"Error creating user: {e}")


# Read all users
@router.get("/", response_model=Page[UserDisplay])
def get_all_users(
    user_filter: Optional[UserFilter] = FilterDepends(UserFilter),
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    """
    Get a list of users
    - **search** can be the 'name' or the 'email' of the user.
    """
    try:
        return services.get_all_users(db, user_filter)
    except Exception as e:
        raise Exception(f"Error getting users: {e}")


# Read one user
@router.get("/{id}", response_model=UserDisplay)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return services.get_user(db, id)
    except HTTPException as e:
        raise e


# Update user
@router.post("/{id}/update")
def update_user(
    id: int,
    request: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return services.update_user(db, id, request)
    except HTTPException as e:
        raise e


# Delete user
@router.get("/{id}/delete")
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    try:
        return services.delete_user(db, id)
    except HTTPException as e:
        raise e

