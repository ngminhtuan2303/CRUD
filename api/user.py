from fastapi import APIRouter, HTTPException
from typing import List
from schemas import User
from services import create_user, get_user, update_user, delete_user, list_users

router = APIRouter()

@router.post("/users", response_model=User)
def create_user_api(user: User):
    return create_user(user)

@router.get("/users/{user_id}", response_model=User)
def get_user_api(user_id: str):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User)
def update_user_api(user_id: str, user: User):
    updated_user = update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
def delete_user_api(user_id: str):
    result = delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.get("/users", response_model=List[User])
def list_users_api():
    return list_users()
