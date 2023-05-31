from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr

    @validator("gender")
    def validate_gender(cls, v):
        if v.lower() not in ["male", "female"]:
            raise ValueError("Invalid gender, must be 'male' or 'female'")
        return v.lower()

class UserUpdate(BaseModel):
    full_name: Optional[str]
    birthday: Optional[datetime]
    gender: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    email: Optional[EmailStr]
    introduction: Optional[str]

class UserInDB(UserCreate):
    id: str
    introduction: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class UserOut(BaseModel):
    id: str
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: Optional[str] = None
    created_at: datetime
    updated_at: datetime
