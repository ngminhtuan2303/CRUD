#### Tạo 1 bộ API CRUD về user

Thông tin người dùng:
ID: auto gen (dùng uuidv4)
Họ tên
Ngày sinh
Giới tính
Số đt
Địa chỉ
Email (unique)
Giới thiệu
created_at
updated_at

#### API: 
Tạo 1 user (POST /api/v1/user)
Get list (GET /api/v1/user) Query theo họ tên, giới tính
Get detail 1 user bằng ID (GET /api/v1/user/:id)
Update tất cả thông tin của 1 user (PUT /api/v1/user/:id)
Xóa 1 user (DEL /api/v1/user/:id)

#### Yêu cầu: 
Tự fake 1,2 người dùng xong lưu vào 1 biến global 
Tạo model cho request body và response bằng pydantic
Chia các tầng 
api - tạo các API bằng fastapi
schemas - Lưu các model pydantic
services - Xử lý các tác vụ mà nhận được từ api và trả kết quả

