# Togogo Backend Test – Django (Employees API)

Hướng dẫn cài đặt, chạy và test API quản lý nhân viên (Employees + WorkSchedule) bằng Django + Django REST Framework.

---

## 1. Yêu cầu

- Python >= 3.10
- pip
- virtualenv (tùy chọn)
- PostgreSQL (hoặc SQLite để chạy local)
- Git (nếu clone project)
- (Tùy chọn) Postman hoặc cURL để test API

---

## 2. Cài đặt môi trường

### 2.1 Clone project

```bash
git clone <link-repo-của-bạn>
cd <tên-folder>
```

### 2.2 Tạo virtual environment và kích hoạt

```bash
# Tạo virtualenv
python -m venv venv

# Kích hoạt trên Windows
venv\Scripts\activate

# Kích hoạt trên macOS/Linux
source venv/bin/activate
```

### 2.3 Cài đặt dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Cấu hình Database

### 3.1 SQLite (mặc định)

Không cần thay đổi gì, Django sẽ tạo file `db.sqlite3`.

### 3.2 PostgreSQL (tùy chọn)

Tạo database và user:

Trong `settings.py`:

```python
import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
```

---

## 4. Áp dụng migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Chạy server

```bash
python manage.py runserver
```

Mặc định server chạy trên: `http://127.0.0.1:8000/`

---

## 6. API Documentation

### 6.1 Employee APIs

#### **GET** `/api/employees/`

Lấy danh sách tất cả nhân viên với tính năng lọc và tìm kiếm.

**Query Parameters:**

- `department` (string, optional): Lọc theo phòng ban (tìm kiếm chính xác, không phân biệt hoa thường)
- `position` (string, optional): Lọc theo vị trí công việc (tìm kiếm chứa chuỗi)
- `q` (string, optional): Tìm kiếm theo tên hoặc email (tìm kiếm chứa chuỗi)
- `start_date_gte` (date, optional): Lọc nhân viên có ngày bắt đầu từ ngày chỉ định trở đi (format: YYYY-MM-DD)

**Response:**

```json
[
  {
    "id": 1,
    "name": "Nguyễn Văn A",
    "email": "nguyenvana@company.com",
    "department": "IT",
    "position": "Backend Developer",
    "start_date": "2024-01-15"
  },
  {
    "id": 2,
    "name": "Trần Thị B",
    "email": "tranthib@company.com",
    "department": "HR",
    "position": "HR Manager",
    "start_date": "2023-12-01"
  }
]
```

**Ví dụ sử dụng:**

```bash
# Lấy tất cả nhân viên
curl -X GET "http://127.0.0.1:8000/api/employees/"

# Lọc theo phòng ban IT
curl -X GET "http://127.0.0.1:8000/api/employees/?department=IT"

# Tìm kiếm theo tên hoặc email
curl -X GET "http://127.0.0.1:8000/api/employees/?q=nguyen"

# Lọc theo nhiều điều kiện
curl -X GET "http://127.0.0.1:8000/api/employees/?department=IT&position=developer&start_date_gte=2024-01-01"
```

#### **POST** `/api/employees/`

Tạo nhân viên mới.

**Request Body:**

```json
{
  "name": "Lê Văn C",
  "email": "levanc@company.com",
  "department": "Marketing",
  "position": "Marketing Specialist",
  "start_date": "2024-03-01"
}
```

**Response (201 Created):**

```json
{
  "id": 3,
  "name": "Lê Văn C",
  "email": "levanc@company.com",
  "department": "Marketing",
  "position": "Marketing Specialist",
  "start_date": "2024-03-01"
}
```

**Ví dụ sử dụng:**

```bash
curl -X POST "http://127.0.0.1:8000/api/employees/" \
     -H "Content-Type: application/json" \
     -d '{
         "name": "Lê Văn C",
         "email": "levanc@company.com",
         "department": "Marketing",
         "position": "Marketing Specialist",
         "start_date": "2024-03-01"
     }'
```

### 6.2 Work Schedule API

#### **POST** `/api/work-schedule/`

Cập nhật hoặc thêm mới lịch làm việc cho nhân viên.

**Request Body:**

```json
{
  "employee_id": 1,
  "work_day": "2024-03-15",
  "shift": "morning"
}
```

**Response (200 OK):**

```json
{
  "message": "Đã cập nhật",
  "data": {
    "employee_id": 1,
    "work_day": "2024-03-15",
    "shift": "morning"
  }
}
```

hoặc nếu tạo mới:

```json
{
  "message": "Đã thêm mới",
  "data": {
    "employee_id": 1,
    "work_day": "2024-03-15",
    "shift": "morning"
  }
}
```

**Ví dụ sử dụng:**

```bash
curl -X POST "http://127.0.0.1:8000/api/work-schedule/" \
     -H "Content-Type: application/json" \
     -d '{
         "employee_id": 1,
         "work_day": "2024-03-15",
         "shift": "morning"
     }'
```

---

## 7. Testing với Postman

### 7.1 Import Collection

Tạo một collection mới trong Postman với các request sau:

1. **Get All Employees**

   - Method: GET
   - URL: `{{base_url}}/api/employees/`

2. **Get Employees with Filters**

   - Method: GET
   - URL: `{{base_url}}/api/employees/?department=IT&q=nguyen`

3. **Create Employee**

   - Method: POST
   - URL: `{{base_url}}/api/employees/`
   - Body: raw JSON

4. **Upsert Work Schedule**
   - Method: POST
   - URL: `{{base_url}}/api/work-schedule/`
   - Body: raw JSON

### 7.2 Environment Variables

Tạo environment với variable:

- `base_url`: `http://127.0.0.1:8000`

---

## 8. Error Handling

### Common HTTP Status Codes:

- `200 OK`: Request thành công
- `201 Created`: Tạo resource thành công
- `400 Bad Request`: Dữ liệu request không hợp lệ
- `404 Not Found`: Resource không tìm thấy
- `500 Internal Server Error`: Lỗi server

### Error Response Format:

```json
{
  "error": "Validation failed",
  "details": {
    "email": ["This field is required."],
    "start_date": ["Enter a valid date."]
  }
}
```
