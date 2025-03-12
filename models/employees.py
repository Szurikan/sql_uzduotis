from sqlalchemy import Column, Integer, String, Date, Float, func, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from database.config import Base


class Employee(Base): # Person paveldi base klase
    __tablename__ = 'employees' # lenteles pavadinimas duomenu bazeje

    id = Column(Integer, primary_key=True, autoincrement=True) # kuriame savybes
    name = Column(String(50), nullable=False) # nullable = not null
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    job_position = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False, default=date.today)
    department_id = Column(Integer, ForeignKey('departments.id', use_alter=True), nullable = True)
    
    managed_departments = relationship("Department", back_populates="manager", foreign_keys="Department.manager_id")
    department = relationship("Department", back_populates="employees", foreign_keys=[department_id])

    project_associations = relationship('EmployeeProject', back_populates='employee')



    def __str__(self):
        return f"{self.id}. {self.name} {self.last_name} - gimė {self.birth_date} - pradejo dirbti {self.start_date} pozicijoje {self.job_position}"

    def __repr__(self):
        return f"{self.id}. {self.name} {self.last_name}"

# Department.employees = relationship("Employee", back_populates="department")