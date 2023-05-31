# from pydantic import BaseModel, validator, EmailStr
# from datetime import datetime
# from uuid import uuid4

# class User(BaseModel):
#     id: str
#     full_name: str
#     birthday: datetime
#     gender: str
#     phone_number: str
#     address: str
#     email: EmailStr
#     introduction: str = None
#     created_at: datetime = datetime.now()
#     updated_at: datetime = datetime.now()

#     @validator("gender")
#     def validate_gender(cls, v):
#         if v.lower() not in ["male", "female"]:
#             raise ValueError("Invalid gender, must be 'male' or 'female'")
#         return v.lower()

#     def __init__(self, **kwargs):
#         if 'id' not in kwargs:
#             kwargs['id'] = str(uuid4())
#         super().__init__(**kwargs)

# class UserCreate(BaseModel):
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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator, EmailStr
from uuid import UUID, uuid4


class UserBase(BaseModel):
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: Optional[str] = None

    @validator("gender")
    def validate_gender(cls, v):
        if v.lower() not in ["male", "female"]:
            raise ValueError("Invalid gender, must be 'male' or 'female'")
        return v.lower()
    

class UserCreate(BaseModel):
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: Optional[str] = None
    
    @validator("gender")
    def validate_gender(cls, v):
        if v.lower() not in ["male", "female"]:
            raise ValueError("Invalid gender, must be 'male' or 'female'")
        return v.lower()
    
    # Sử dụng hàm uuid4 để tạo mới UUID cho User
    id: UUID = uuid4()


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    birthday: Optional[datetime] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    introduction: Optional[str] = None
    
    @validator("gender")
    def validate_gender(cls, v):
        if v and v.lower() not in ["male", "female"]:
            raise ValueError("Invalid gender, must be 'male' or 'female'")
        return v
    
    # Sử dụng hàm uuid4 để update UUID của User
    id: UUID = uuid4()


class User(UserBase):
    # Sử dụng hàm uuid4 để tạo mới UUID cho User
    id: UUID = uuid4()
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
