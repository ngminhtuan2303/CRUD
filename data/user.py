from schemas.user import User
from datetime import datetime
from uuid import uuid4

users = [
    User(
        id=str(uuid4()),
        full_name="Nguyễn Văn A",
        birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        gender="Male",
        phone_number="0123456789",
        address="Hà Nội",
        email="nguyenvana@gmail.com",
    ),
    User(
        id=str(uuid4()),
        full_name="Lê Thị B",
        birthday=datetime.strptime("1995-02-01", "%Y-%m-%d"),
        gender="Female",
        phone_number="0987654321",
        address="Sài Gòn",
        email="lethib@gmail.com",
        introduction="I'm a software engineer",
    ),
]