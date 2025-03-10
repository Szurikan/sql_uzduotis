from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.config import Base


class Department(Base):
    __tablename__= 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    manager_id = Column(Integer, nullable=True)
   
    employees = relationship("Employee", back_populates="department")

    def __str__(self):
        return f"{self.id}. {self.name}"

    def __repr__(self):
        return f"{self.id}. {self.name}"

