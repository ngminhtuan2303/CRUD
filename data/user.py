from datetime import datetime
from schemas.user import User,UserCreate

users_data = [
    User(
        ho_ten="Nguyen Van A",
        ngay_sinh=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        gioi_tinh="Nam",
        so_dt="0123456789",
        dia_chi="Ha Noi",
        email="nguyenvana@example.com",
        gioi_thieu="",
    ),
    User(
        ho_ten="Le Thi B",
        ngay_sinh=datetime.strptime("1995-02-01", "%Y-%m-%d"),
        gioi_tinh="Nu",
        so_dt="0987654321",
        dia_chi="Ho Chi Minh",
        email="lethib@example.com",
        gioi_thieu="",
    ),
]
