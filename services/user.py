from typing import List
from schemas.user import User, UserCreate, UserUpdate
from datetime import datetime
from fastapi import HTTPException
from data.user import users


class UserService:
    
    def create_user(user: User) -> UserCreate:
        for u in users:
            if u.email == user.email:
                raise HTTPException(status_code=400, detail="Email already exists")
        users.append(user)
        return user

    
    def list_users(full_name: str = None, gender: str = None) -> List[User]:
        if full_name and gender:
            return [
                user for user in users
                if user.full_name.lower().startswith(full_name.lower()) and user.gender == gender.lower()
            ]
        elif full_name:
            return [user for user in users if user.full_name.lower().startswith(full_name.lower())]
        elif gender:
            return [user for user in users if user.gender == gender.lower()]
        return users

    
    def get_user(user_id: str) -> User:
        for user in users:
            if user.id == user_id:
                return user
        raise HTTPException(status_code=404, detail="User not found")

    
    def update_user(user_id: str, user_update: User) -> UserUpdate:
        for i, user in enumerate(users):
            if user.id == user_id:
                user.full_name = user_update.full_name
                user.birthday = user_update.birthday
                user.gender = user_update.gender
                user.phone_number = user_update.phone_number
                user.address = user_update.address
                user.email = user_update.email
                user.introduction = user_update.introduction
                user.updated_at = datetime.now()
                users[i] = user
                return user
        raise HTTPException(status_code=404, detail="User not found")

    
    def delete_user(user_id: str):
        for i, user in enumerate(users):
            if user.id == user_id:
                del users[i]
                return {"message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")
