from fastapi import APIRouter, HTTPException
from schemas.user import User,UserBase,UserCreate,UserUpdate
from services.user import create_user,get_user,get_users,update_user,delete_user
from typing import List
router = APIRouter()

# Users CRUD
@router.post("/user", response_model=User)
def create_user(user: UserCreate):
    return create_user(user)

@router.get("/user", response_model=List[User])
def list_users(skip: int = 0, limit: int = 100):
    return get_users(skip=skip, limit=limit)

@router.get("/user/{user_id}", response_model=User)
def get_user(user_id: str):
    db_user = get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/user/{user_id}", response_model=User)
def update_user(user_id: str, user: UserUpdate):
    db_user = update_user(user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/user/{user_id}")
def delete_user(user_id: str):
    result = delete_user(user_id=user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
