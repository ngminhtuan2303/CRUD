#data
from schemas.user import User
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://root:Tuan23032001@localhost:27018/')
db = client["CRUD"]
collection = db["users"]

# Global variable
# users = [
#     User(
#         full_name="Nguyễn Văn A",
#         birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
#         gender="Male",
#         phone_number="0123456789",
#         address="Hà Nội",
#         email="nguyenvana@gmail.com",
#     ),
#     User(
#         full_name="Lê Thị B",
#         birthday=datetime.strptime("1995-02-01", "%Y-%m-%d"),
#         gender="Female",
#         phone_number="0987654321",
#         address="Sài Gòn",
#         email="lethib@gmail.com",
#         introduction="I'm a software engineer",
#     ),
# ]

# users = collection.insert_many(result)