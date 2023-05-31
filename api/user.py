from fastapi import APIRouter, HTTPException
from typing import Optional
from schemas.user import User, UserCreate, UserUpdate
from services.user import create_user, list_users, get_user, update_user, delete_user
from typing import List

router = APIRouter()


@router.post('/user', response_model=User)
def create_user(user: UserCreate):
    try:
        return create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/user', response_model=List[User])
def list_users(full_name: Optional[str] = None, gender: Optional[str] = None):
    return List[User](users=list_users(full_name, gender))


@router.get('/user/{user_id}', response_model=User)
def get_user(user_id: str):
    try:
        return get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put('/user/{user_id}', response_model=User)
def update_user(user_id: str, user_update: UserUpdate):
    try:
        return update_user(user_id, user_update)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete('/user/{user_id}')
def delete_user(user_id: str):
    try:
        delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
        
    return {'message': 'User deleted'}
