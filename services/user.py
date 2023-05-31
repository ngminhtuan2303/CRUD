from uuid import uuid4
from datetime import datetime
from typing import List
from schemas.user import UserCreate, UserUpdate, UserInDB, UserOut

class UserService:
    def __init__(self):
        self.users = [
            UserInDB(
                id=str(uuid4()),
                full_name="Nguyễn Văn A",
                birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
                gender="Male",
                phone_number="0123456789",
                address="Hà Nội",
                email="nguyenvana@gmail.com",
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            UserInDB(
                id=str(uuid4()),
                full_name="Lê Thị B",
                birthday=datetime.strptime("1995-02-01", "%Y-%m-%d"),
                gender="Female",
                phone_number="0987654321",
                address="Sài Gòn",
                email="lethib@gmail.com",
                introduction="I'm a software engineer",
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
        ]

    def create_user(self, user_create: UserCreate) -> UserOut:
        for u in self.users:
            if u.email == user_create.email:
                raise ValueError("Email already exists")
        user_db = UserInDB(
            id=str(uuid4()),
            **user_create.dict(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.users.append(user_db)
        return user_db

    def list_users(self, full_name: str = None, gender: str = None) -> List[UserOut]:
        if full_name and gender:
            return [
                self._convert_db_to_out(user) for user in self.users
                if user.full_name.lower().startswith(full_name.lower()) and user.gender == gender.lower()
            ]
        elif full_name:
            return [self._convert_db_to_out(user) for user in self.users if user.full_name.lower().startswith(full_name.lower())]
        elif gender:
            return [self._convert_db_to_out(user) for user in self.users if user.gender == gender.lower()]
        return [self._convert_db_to_out(user) for user in self.users]

    def get_user(self, user_id: str) -> UserOut:
        for user in self.users:
            if user.id == user_id:
                return self._convert_db_to_out(user)
        raise ValueError("User not found")

    def update_user(self, user_id: str, user_update: UserUpdate) -> UserOut:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                user_dict = user.dict()
                user_dict.update(user_update.dict(skip_defaults=True))
                user_db = UserInDB(
                    **user_dict,
                    updated_at=datetime.now()
                )
                self.users[i] = user_db
                return self._convert_db_to_out(user_db)
        raise ValueError("User not found")

    def delete_user(self, user_id: str) -> bool:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False

    def _convert_db_to_out(self, user_db: UserInDB) -> UserOut:
        return UserOut(**user_db.dict())
