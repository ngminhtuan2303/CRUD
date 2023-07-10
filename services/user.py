# services
from typing import List, Union
from schemas.user import User, UserCreate, UserUpdate
from datetime import datetime
from fastapi import HTTPException
from data.user import collection
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId


class UserService:
    
    # def create_user(user: UserCreate) -> UserCreate:
    #     user_dict = user.dict()
    #     user_dict["_id"] = ObjectId()
    #     user_dict["created_at"] = datetime.utcnow()
    #     user_dict["updated_at"] = datetime.utcnow()
    #     try:
    #         collection.insert_one(user_dict)
    #     except DuplicateKeyError:
    #         return None
    #     return UserCreate(**user_dict)

    def create_user(user: UserCreate) -> Union[UserCreate, None]:
        user_dict = user.dict()
        user_dict["_id"] = ObjectId()
        user_dict["created_at"] = datetime.utcnow()
        user_dict["updated_at"] = datetime.utcnow()

        # Kiểm tra email đã tồn tại hay chưa
        existing_user = collection.find_one({"email": user.email})
        if existing_user:
            return None

        try:
            collection.insert_one(user_dict)
        except DuplicateKeyError:
            return None

        return UserCreate(**user_dict)


    
    def list_users(full_name: str = None, gender: str = None) -> List[User]:
        query = {}
        if full_name:
            query["full_name"] = {"$regex": full_name, "$options": "i"}
        if gender:
            query["gender"] = gender
        users = [User(**user) for user in collection.find(query)]
        return users

    
    def get_user(user_id: str) -> User:
        _id = ObjectId(user_id)
        print(_id)
        user = collection.find_one({"_id": _id})
        if user:
            return User(**user)
        raise HTTPException(status_code=404, detail="User not found")
    
    # def update_user(user_id: str, user_update: User) -> UserUpdate:
    #     user_dict = user_update.dict()
    #     user_dict["updated_at"] = datetime.utcnow()
    #     result = collection.update_one(
    #         {"_id": ObjectId(user_id)}, {"$set": user_dict}
    #     )
    #     if result.modified_count:
    #         user_dict["_id"] = user_id
    #         return User(**user_dict)
    #     raise HTTPException(status_code=404, detail="User not found")

    def update_user(user_id: str, user_update: User) -> Union[UserUpdate, None]:
        user_dict = user_update.dict()
        user_dict["updated_at"] = datetime.utcnow()

        # Kiểm tra email đã tồn tại và khác với email của user cần cập nhật hay chưa
        existing_user = collection.find_one({"email": user_update.email})
        if existing_user and existing_user["_id"] != ObjectId(user_id):
            return None

        result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})

        if result.modified_count:
            user_dict["_id"] = user_id
            return User(**user_dict)
        raise HTTPException(status_code=404, detail="User not found")

    
    def delete_user(user_id: str):
        result = collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count:
            return {"message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")
    
    