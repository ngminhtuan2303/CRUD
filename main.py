from fastapi import FastAPI, HTTPException
from fastapi.param_functions import Query
from uuid import uuid4
from datetime import datetime
from typing import List
from pydantic import BaseModel, validator, EmailStr

class User(BaseModel):
    id: str
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: str = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @validator("gender")
    def validate_gender(cls, v):
        if v.lower() not in ["male", "female"]:
            raise ValueError("Invalid gender, must be 'male' or 'female'")
        return v.lower()

    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        super().__init__(**kwargs)

# class UserOut(BaseModel):
#     id: str
#     full_name: str
#     birthday: datetime
#     gender: str
#     phone_number: str
#     address: str
#     email: EmailStr
#     introduction: str = None
#     created_at: datetime
#     updated_at: datetime


# class UserUpdate(BaseModel):
#     full_name: str
#     birthday: datetime
#     gender: str
#     phone_number: str
#     address: str
#     email: EmailStr
#     introduction: str = None


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

app = FastAPI()

@app.post("/api/v1/user", response_model=User)
def create_user(user: User):
    for u in users:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    users.append(user)
    return user

@app.get("/api/v1/user", response_model=List[User])
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

@app.get("/api/v1/user/{user_id}", response_model=User)
def get_user(user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/v1/user/{user_id}", response_model=User)
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

@app.delete("/api/v1/user/{user_id}")
def delete_user(user_id: str):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


# Trong đó, chúng ta đã:
# Định nghĩa các model Pydantic để validate request và response body.
# Sử dụng uuid4 để auto generate ID cho User.
# Sử dụng datetime để lưu ngày giờ tạo và cập nhật User.
# Sử dụng typing để định nghĩa kiểu dữ liệu trả về cho API endpoints.
# Sử dụng HTTPException của FastAPI để quản lý các HTTP error codes và thông báo lỗi.
# Sử dụng các endpoint như POST, GET, PUT và DELETE để xử lý các yêu cầu thêm, sửa, xóa và truy vấn User.
# Chú ý: Đoạn mã trên chỉ để minh hoạ cho việc áp dụng các tầng. Thông tin về user chỉ lưu trong memory, không lưu trên cơ sở dữ liệu. 
# Để triển khai trên môi trường sản phẩm, chúng ta cần định nghĩa các lớp xử lý cho cơ sở dữ liệu và di chuyển các tác vụ liên quan đến cơ sở dữ liệu sang các lớp này.