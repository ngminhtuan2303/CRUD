from fastapi import APIRouter, Depends, HTTPException
from typing import List
from services.user import UserService
from schemas.user import UserCreate, UserUpdate, UserOut

router = APIRouter()
user_service = UserService()

@router.post("/", response_model=UserOut)
def create_user(user_create: UserCreate, user_service: UserService = Depends()):
    try:
        return user_service.create_user(user_create)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=exc.args[0])

@router.get("/", response_model=List[UserOut])
def list_users(full_name: str = None, gender: str = None, user_service: UserService = Depends()):
    return user_service.list_users(full_name, gender)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: str, user_service: UserService = Depends()):
    user_out = user_service.get_user(user_id)
    if user_out:
        return user_out
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: str, user_update: UserUpdate, user_service: UserService = Depends()):
    user_out = user_service.update_user(user_id, user_update)
    if user_out:
        return user_out
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: str, user_service: UserService = Depends()):
    if user_service.delete_user(user_id):
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
