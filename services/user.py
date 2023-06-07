# services
from typing import List
from schemas.user import User, UserCreate, UserUpdate
from datetime import datetime
from fastapi import HTTPException
from data.user import collection
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId


class UserService:
    
    def create_user(user: User) -> UserCreate:
        # for u in users:
        #     if u.email == user.email:
        #         raise HTTPException(status_code=400, detail="Email already exists")
        # users.append(user)
        # return user
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
        # if full_name and gender:
        #     return [
        #         user for user in users
        #         if user.full_name.lower().startswith(full_name.lower()) and user.gender == gender.lower()
        #     ]
        # elif full_name:
        #     return [user for user in users if user.full_name.lower().startswith(full_name.lower())]
        # elif gender:
        #     return [user for user in users if user.gender == gender.lower()]
        # return users
        query = {}
        if full_name:
            query["full_name"] = {"$regex": full_name, "$options": "i"}
        if gender:
            query["gender"] = gender
        users = [User(**user) for user in collection.find(query)]
        return users

    
    def get_user(user_id: str) -> User:
        # for user in users:
        #     if user.id == user_id:
        #         return user
        # raise HTTPException(status_code=404, detail="User not found")
        _id = ObjectId(user_id)
        user = collection.find_one({"_id": _id})
        if user:
            print(user)
            return User(**user)
        raise HTTPException(status_code=404, detail="User not found")
    
    def update_user(user_id: str, user_update: User) -> UserUpdate:
        # for i, user in enumerate(users):
        #     if user.id == user_id:
        #         user.full_name = user_update.full_name
        #         user.birthday = user_update.birthday
        #         user.gender = user_update.gender
        #         user.phone_number = user_update.phone_number
        #         user.address = user_update.address
        #         user.email = user_update.email
        #         user.introduction = user_update.introduction
        #         user.updated_at = datetime.now()
        #         users[i] = user
        #         return user
        # raise HTTPException(status_code=404, detail="User not found")
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
        # for i, user in enumerate(users):
        #     if user.id == user_id:
        #         del users[i]
        #         return {"message": "User deleted"}
        # raise HTTPException(status_code=404, detail="User not found")
        result = collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count:
            return {"message": "User deleted"}
        raise HTTPException(status_code=404, detail="User not found")
