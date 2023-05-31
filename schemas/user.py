from typing import List
from datetime import datetime
from pydantic import BaseModel, validator, EmailStr

class UserBase(BaseModel):
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: str = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
