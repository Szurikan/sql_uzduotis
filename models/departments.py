from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config import Base


class Department(Base):
    __tablename__= 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    manager_id = Column(Integer, ForeignKey("employees.id", use_alter=True), nullable=True)
   
    manager = relationship("Employee", back_populates="managed_departments", foreign_keys=[manager_id])
    employees = relationship("Employee", back_populates="department", foreign_keys="Employee.department_id")
    

    def __str__(self):
        return f"{self.id}. {self.name}"

    def __repr__(self):
        return f"{self.id}. {self.name}"

