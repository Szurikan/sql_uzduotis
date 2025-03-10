from services.app_service import get_string_input, get_int_input
from database.config import session_maker
from models.departments import Department
from models.employees import Employee
from sqlalchemy import select

def add_department():
    
    name = get_string_input("Irasykite departamento pavadinima: ")
    with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
        department = Department(name=name)
        session.add(department)
        session.commit()
    print("Departamentas sekmingai pridetas.")

def show_department_employees():

    department_id = get_int_input("Irasykite departamento numeri: ")
    with session_maker() as session:
        department = session.get(Department, department_id)

        if not department:
            print("Departamentas nerastas")
            return
        
        employees = session.query(Employee).filter(Employee.department_id == Department.id).all()

        if not employees:
            print("Darbuotojas nepriklauso departamentui")
            return
        
        print(f"Darbuotojai departamente:")
        for employee in employees:
            print(f"{employee.name} {employee.last_name} - {employee.job_position}")