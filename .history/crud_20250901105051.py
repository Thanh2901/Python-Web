from sqlalchemy.orm import Session
from models import Employee, WorkSchedule
from schemas import EmployeeCreate, WorkScheduleUpsert
from datetime import date

# ========== Employee CRUD ==========
def create_employee(db: Session, employee: EmployeeCreate):
    if db.query(Employee).filter(Employee.email == employee.email).first():
        return None
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees_by_department(db: Session, department: str, skip: int = 0, limit: int = 10):
    return db.query(Employee).filter(Employee.department == department).offset(skip).limit(limit).all()


# ========== Work Schedule CRUD ==========
def upsert_work_schedule(db: Session, data: WorkScheduleUpsert):
    schedule = db.query(WorkSchedule).filter(
        WorkSchedule.employee_id == data.employee_id,
        WorkSchedule.work_day == data.work_day
    ).first()

    if schedule:
        schedule.shift = data.shift
        db.commit()
        db.refresh(schedule)
        return schedule, "updated"
    else:
        new_schedule = WorkSchedule(**data.dict())
        db.add(new_schedule)
        db.commit()
        db.refresh(new_schedule)
        return new_schedule, "created"
