from pydantic import BaseModel, validator, EmailStr
from datetime import datetime
from uuid import uuid4

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

class UserOut(BaseModel):
    id: str
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: str = None
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    full_name: str
    birthday: datetime
    gender: str
    phone_number: str
    address: str
    email: EmailStr
    introduction: str = None