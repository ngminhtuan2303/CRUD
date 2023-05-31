from typing import List
from uuid import uuid4
from datetime import datetime
from fastapi.exceptions import HTTPException
from schemas.user import User,UserBase,UserCreate,UserUpdate

# Global variable
users = [
    {
        "id": str(uuid4()), 
        "full_name":"Nguyễn Văn A", 
        "birthday": datetime.strptime("1990-01-01", "%Y-%m-%d"), 
        "gender":"male",
        "phone_number":"0123456789",
        "address":"Hà Nội",
        "email":"nguyenvana@gmail.com",
        "created_at":datetime.now(),
        "updated_at":datetime.now()
    },
    {
        "id": str(uuid4()), 
        "full_name":"Lê Thị B", 
        "birthday":datetime.strptime("1995-02-01", "%Y-%m-%d"), 
        "gender":"female",
        "phone_number":"0987654321",
        "address":"Sài Gòn",
        "email":"lethib@gmail.com",
        "introduction":"I'm a software engineer", 
        "created_at":datetime.now(),
        "updated_at":datetime.now()
    }
]

# Users CRUD
def get_user(user_id: str):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def get_users(skip: int = 0, limit: int = 100):
    return users[skip:skip+limit]

def create_user(user: UserCreate):
    for u in users:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    db_user = user.dict()
    db_user["id"] = str(uuid4())
    db_user["created_at"] = datetime.now()
    db_user["updated_at"] = datetime.now()
    users.append(db_user)
    return db_user

def update_user(user_id: str, user: UserUpdate):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            for attr in user.dict(exclude_unset=True):
                users[i][attr] = user.dict()[attr]
            users[i]["updated_at"] = datetime.now()
            return users[i]
    return None

def delete_user(user_id: str):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            del users[i]
            return True
    return None
