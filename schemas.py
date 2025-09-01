from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

# ===== Employee =====
class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    position: Optional[str] = None
    department: Optional[str] = None
    start_date: Optional[date] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    position: Optional[str]
    department: Optional[str]
    start_date: Optional[date]

    class Config:
        orm_mode = True


# ===== Work Schedule =====
class WorkScheduleUpsert(BaseModel):
    employee_id: int
    work_day: date
    shift: str

class WorkScheduleResponse(BaseModel):
    id: int
    employee_id: int
    work_day: date
    shift: str

    class Config:
        orm_mode = True
