from typing import List
from schemas import User
from datetime import datetime
from uuid import uuid4
from data import users


def create_user(user: User) -> User:
    user.id = str(uuid4())
    user.created_at = datetime.now()
    user.updated_at = datetime.now()
    users.append(user)
    return user

def get_user(user_id: str) -> User:
    for user in users:
        if user.id == user_id:
            return user
    return None

def update_user(user_id: str, user: User) -> User:
    for i, u in enumerate(users):
        if u.id == user_id:
            user.created_at = u.created_at
            user.updated_at = datetime.now()
            users[i] = user
            return user
    return None

def delete_user(user_id: str) -> bool:
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return True
    return False

def list_users() -> List[User]:
    return users
