# from typing import List, Optional
# from uuid import uuid4
# from datetime import datetime
# from schemas.user import User, UserCreate, UserUpdate
# from fastapi import HTTPException


# users = [
#     User(
#         full_name="Nguyễn Văn A",
#         birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
#         gender="male",
#         phone_number="0123456789",
#         address="Hà Nội",
#         email="nguyenvana@gmail.com",
#     ),
#     User(
#         full_name="Lê Thị B",
#         birthday=datetime.strptime("1995-02-01", "%Y-%m-%d"),
#         gender="female",
#         phone_number="0987654321",
#         address="Sài Gòn",
#         email="lethib@gmail.com",
#         introduction="I'm a software engineer",
#     ),
# ]


# def create_user(user: UserCreate):
#     for u in users:
#         if u.email == user.email:
#             raise HTTPException(status_code=400, detail="Email already exists")
#     users.append(user)
#     return user

# def list_users(full_name: str = None, gender: str = None):
#     if full_name and gender:
#         return [
#             user for user in users
#             if user.full_name.lower().startswith(full_name.lower()) and user.gender == gender.lower()
#         ]
#     elif full_name:
#         return [user for user in users if user.full_name.lower().startswith(full_name.lower())]
#     elif gender:
#         return [user for user in users if user.gender == gender.lower()]
#     return users


# def get_user(user_id: str):
#     for user in users:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=404, detail="User not found")


# def update_user(user_id: str, user_update: UserUpdate):
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             user.full_name = user_update.full_name
#             user.birthday = user_update.birthday
#             user.gender = user_update.gender
#             user.phone_number = user_update.phone_number
#             user.address = user_update.address
#             user.email = user_update.email
#             user.introduction = user_update.introduction
#             user.updated_at = datetime.now()
#             users[i] = user
#             return user
#     raise HTTPException(status_code=404, detail="User not found")


# def delete_user(user_id: str):
#     for i, user in enumerate(users):
#         if user.id == user_id:
#             del users[i]
#             return {"message": "User deleted"}
#     raise HTTPException(status_code=404, detail="User not found")

from datetime import datetime
from typing import Dict, List
from uuid import UUID, uuid4

# Định nghĩa các Pydantic models cho User
from schemas.user import UserBase, UserCreate, UserUpdate, User

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, user_in: UserCreate) -> User:
        # Sử dụng uuid4() để tạo ra UUID ngẫu nhiên cho User mới
        user_id = uuid4()
        now = datetime.utcnow()
        # Tạo đối tượng User từ đối tượng UserCreate và gán UUID
        user = User(id=user_id, created_at=now, updated_at=now, **user_in.dict())
        # Lưu đối tượng User vào dict
        self.users[user_id] = user
        # Trả về đối tượng User được tạo
        return user

    def get_user(self, id: UUID) -> User:
        # Nếu không tìm thấy user, trả về None
        if id not in self.users:
            return None
        # Trả về user đã tìm thấy
        return self.users[id]

    def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        # Lấy toàn bộ user từ dict
        all_users = list(self.users.values())
        # Trả về phần tương ứng theo skip và limit
        return all_users[skip : skip + limit]

    def update_user(self, user_id: UUID, user_in: UserUpdate) -> User:
        # Nếu không tìm thấy user, trả về None
        if user_id not in self.users:
            return None
        # Lấy thông tin user được cập nhật từ đối tượng UserUpdate
        user = self.users[user_id]
        update_data = user_in.dict(exclude_unset=True)
        # Cập nhật thông tin user
        for field in update_data:
            setattr(user, field, update_data[field])
        user.updated_at = datetime.utcnow()
        # Trả về user được cập nhật
        return user

    def delete_user(self, id: UUID) -> bool:
        # Nếu không tìm thấy user, trả về False
        if id not in self.users:
            return False
        # Xóa user khỏi dict
        del self.users[id]
        # Trả về True nếu user đã xóa được và False nếu không
        return True
