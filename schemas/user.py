from pydantic import BaseModel, validator, EmailStr
from datetime import datetime
from uuid import uuid4


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

    @validator("gender")
    def validate_gender(cls, v):
        if v.lower() not in ["male", "female"]:
            raise ValueError("Invalid gender, must be 'male' or 'female'")
        return v.lower()

    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        super().__init__(**kwargs)

        now = datetime.now()
        if 'created_at' not in kwargs:
            kwargs['created_at'] = now

        kwargs['updated_at'] = now
