from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    position = Column(String)
    department = Column(String)
    start_date = Column(Date)

    work_schedules = relationship("WorkSchedule", back_populates="employee")


class WorkSchedule(Base):
    __tablename__ = "work_schedules"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    work_day = Column(Date)
    shift = Column(String)

    employee = relationship("Employee", back_populates="work_schedules")
