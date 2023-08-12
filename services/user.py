# services
from typing import List, Union
from schemas.user import User, UserCreate, UserUpdate
from datetime import datetime
from fastapi import HTTPException
from data.user import collection
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from milvus_collection.user import milvus_collection, insert_data, search_faces
from arcface.ArcFace import ArcFace
import cv2
import numpy as np
from retinaface import RetinaFace
import base64
from schemas.facesearch import FaceSearch, Face



class UserService:

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
            timestamp = user_dict["created_at"].timestamp()
            int64_value = np.int64(timestamp)
            int_value = int(int64_value)


            img_base64 = user_dict["image"]
            # print("anh base64",img_base64)
            
            # Giải mã chuỗi base64 thành dữ liệu bytes
            img_data = base64.b64decode(img_base64)
            # print("anh bytes", img_data)
            # Chuyển dữ liệu bytes thành mảng numpy
            nparr = np.frombuffer(img_data, np.uint8)
            img = cv2.cvtColor(nparr, cv2.COLOR_BGR2RGB)
            # print("anh numpy",nparr)
            
            face_rec = ArcFace()
            
            face_embedding = face_rec.calc_emb(img)
            # print("data",face_embedding.dtype)
            img_vector = np.array2string(face_embedding)
            user_dict["img_vector"] = img_vector
            insert_data(milvus_collection, int64_value, face_embedding.astype(np.float32).tolist())
            user_dict["id_milvus"] = int_value
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
    
    def search_face(face: FaceSearch)->Union[FaceSearch,None]:
        face_dict = face.dict()
        face_dict["searched_at"] = datetime.utcnow()

        img_base64 = face_dict["face"]
        # print("anh base64",img_base64)
        
        # Giải mã chuỗi base64 thành dữ liệu bytes
        img_data = base64.b64decode(img_base64)
        # print("anh bytes", img_data)
        # Chuyển dữ liệu bytes thành mảng numpy
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.cvtColor(nparr, cv2.COLOR_BGR2RGB)
        # print("anh numpy",nparr)

        face_rec = ArcFace()
            
        face_embedding = face_rec.calc_emb(img)
        search_faces(milvus_collection, face_embedding.astype(np.float32).tolist())