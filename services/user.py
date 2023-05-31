from typing import List
from schemas.user import User, UserCreate, UserUpdate
from datetime import datetime
from fastapi import HTTPException

# Global variable
users = [
    User(
        full_name="Nguyễn Văn A",
        birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        gender="Male",
        phone_number="0123456789",
        address="Hà Nội",
        email="nguyenvana@gmail.com",
    ),
    User(
        full_name="Lê Thị B",
        birthday=datetime.strptime("1995-02-01", "%Y-%m-%d"),
        gender="Female",
        phone_number="0987654321",
        address="Sài Gòn",
        email="lethib@gmail.com",
        introduction="I'm a software engineer",
    ),
]


class UserService:
    @staticmethod
    def create_user(user: UserCreate) -> User:
        for u in users:
            if u.email == user.email:
                raise HTTPException(status_code=400, detail="Email already exists")
        user_dict = user.dict()
        u = User(**user_dict)
        users.append(u)
        return u

    @staticmethod
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

    @staticmethod
    def get_user(user_id: str) -> User:
        for user in users:
            if user.id == user_id:
                return user
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def update_user(user_id: str, user_update: UserUpdate) -> User:
        for i, user in enumerate(users):
            if user.id == user_id:
                user_dict = user_update.dict(exclude_unset=True)
                user_dict["updated_at"] = datetime.now()
                updated_user = user.copy(update=user_dict)
                users[i] = updated_user
                return updated_user
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def delete_user(user_id: str):
        for i, user in enumerate(users):
            if user.id == user_id:
                del users[i]
                return {"message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")
