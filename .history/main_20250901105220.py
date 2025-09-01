from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="HR Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# tao nhan vien moi
@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.create_employee(db, employee)
    if not db_employee:
        raise HTTPException(status_code=400, detail="Email đã tồn tại")
    return db_employee

# lay danh sach nhan vien + phan trang
@app.get("/employees", response_model=List[schemas.EmployeeResponse])
def list_employees(department: str = Query(...), skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = crud.get_employees_by_department(db, department, skip, limit)
    return employees

# cap nhat ca lam viec
@app.post("/work-schedule")
def upsert_schedule(schedule: schemas.WorkScheduleUpsert, db: Session = Depends(get_db)):
    result, status = crud.upsert_work_schedule(db, schedule)
    message = "Đã cập nhật lịch làm việc" if status == "updated" else "Đã thêm mới lịch làm việc"
    return {"message": message, "data": result}
