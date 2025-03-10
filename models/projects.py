from sqlalchemy import Column, Integer, String, Date, Float, func
from sqlalchemy.orm import relationship
from datetime import date
from database.config import Base


class Project(Base):
    __tablename__= 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)

    employee_associations = relationship("EmployeeProject", back_populates="project")

    def __str__(self):
        return f"{self.id}. {self.name}"

    def __repr__(self):
        return f"{self.id}. {self.name}"

