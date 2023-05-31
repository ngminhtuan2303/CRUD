from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime
from schemas.user import User, UserCreate, UserUpdate


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


def create_user(user: UserCreate) -> User:
    for u in users:
        if u.email == user.email:
            raise ValueError('Email already exists')
    user = User(**user.dict())
    user.id = uuid4()
    users.append(user)
    return user


def list_users(full_name: Optional[str] = None, gender: Optional[str] = None) -> List[User]:
    results = []
    for user in users:
        if full_name and gender:
            if user.full_name.lower().startswith(full_name.lower()) and user.gender == gender.lower():
                results.append(user)
        elif full_name:
            if user.full_name.lower().startswith(full_name.lower()):
                results.append(user)
        elif gender:
            if user.gender == gender.lower():
                results.append(user)
        else:
            results.append(user)
    return results


def get_user(user_id: UUID) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise ValueError('User not found')


def update_user(user_id: UUID, user_update: UserUpdate) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            user = User(**user_update.dict())
            user.id = user_id
            users[i] = user
            return user
    raise ValueError('User not found')


def delete_user(user_id: UUID) -> None:
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return
    raise ValueError('User not found')
