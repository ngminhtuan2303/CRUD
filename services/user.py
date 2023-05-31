from typing import List, Optional
from uuid import uuid4
from datetime import datetime
from schemas.user import User, UserCreate, UserUpdate
from fastapi import HTTPException


users = [
    User(
        full_name="Nguyễn Văn A",
        birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        gender="male",
        phone_number="0123456789",
        address="Hà Nội",
        email="nguyenvana@gmail.com",
    ),
    User(
        full_name="Lê Thị B",
        birthday=datetime.strptime("1995-02-01", "%Y-%m-%d"),
        gender="female",
        phone_number="0987654321",
        address="Sài Gòn",
        email="lethib@gmail.com",
        introduction="I'm a software engineer",
    ),
]


def create_user(user: User):
    for u in users:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    users.append(user)
    return user

def list_users(full_name: str = None, gender: str = None):
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


def get_user(user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


def update_user(user_id: str, user_update: User):
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
