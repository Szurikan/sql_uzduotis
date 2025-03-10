from database.config import Base
from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.orm import relationship

class EmployeeProject(Base):
    __tablename__ = 'employee_project'
    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)

    employee = relationship('Employee', back_populates='project_associations')
    project = relationship('Project', back_populates='employee_associations')