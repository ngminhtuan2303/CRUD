from fastapi import APIRouter, HTTPException
from typing import List
from schemas.user import User, UserCreate, UserUpdate
from services.user import UserService

router = APIRouter()

@router.post("/api/v1/user", response_model=UserCreate)
def create_user(user: User):
    return UserService.create_user(user)

@router.get("/api/v1/user", response_model=List[User])
def list_users(full_name: str = None, gender: str = None):
    return UserService.list_users(full_name, gender)

@router.get("/api/v1/user/{user_id}", response_model=User)
def get_user(user_id: str):
    return UserService.get_user(user_id)

@router.put("/api/v1/user/{user_id}", response_model=UserUpdate)
def update_user(user_id: str, user_update: User):
    return UserService.update_user(user_id, user_update)

@router.delete("/api/v1/user/{user_id}")
def delete_user(user_id: str):
    return UserService.delete_user(user_id)
