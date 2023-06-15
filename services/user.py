# services
from typing import List
from schemas.user import User, UserCreate, UserUpdate
from datetime import datetime
from fastapi import HTTPException
from data.user import collection
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId


class UserService:
    
    def create_user(user: UserCreate) -> UserCreate:
        user_dict = user.dict()
        user_dict["_id"] = ObjectId()
        user_dict["created_at"] = datetime.utcnow()
        user_dict["updated_at"] = datetime.utcnow()
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
    
    def update_user(user_id: str, user_update: User) -> UserUpdate:
        user_dict = user_update.dict()
        user_dict["updated_at"] = datetime.utcnow()
        result = collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": user_dict}
        )
        if result.modified_count:
            user_dict["_id"] = user_id
            return User(**user_dict)
        raise HTTPException(status_code=404, detail="User not found")
    
    def delete_user(user_id: str):
        result = collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count:
            return {"message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")
    
    