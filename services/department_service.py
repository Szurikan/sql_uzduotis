from services.app_service import get_string_input, get_int_input
from database.config import session_maker
from models.departments import Department
from models.employees import Employee
from sqlalchemy import select
from services.employee_service import show_employees

def add_department():

    name = get_string_input("Irasykite departamento pavadinima: ")
    with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
        department = Department(name=name)
        session.add(department)
        session.commit()
    print("Departamentas sekmingai pridetas.")

def show_departments():
    with session_maker() as session:
        query = select(Department) # gauname objektus
        departments = session.execute(query).scalars().all()
    if departments:
        print(f"Departamentu sarasas: \n")
    for department in departments:
        print(department)
    if not departments:
        print("Departamentu nerasta.")


def show_department_employees():
    show_departments()
    department_id = get_int_input("Irasykite departamento numeri: ")
    with session_maker() as session:
        department = session.get(Department, department_id)

        if not department:
            print("Departamentas nerastas")
            return
        
        employees = session.query(Employee).filter(Employee.department_id == department.id).all()

        if not employees:
            print("Darbuotojas nepriklauso departamentui")
            return
        
        print(f"Darbuotojai departamente:")
        for employee in employees:
            if department.manager_id == employee.id:
                print(f"{employee.name} {employee.last_name} - {employee.job_position} - Departamento vadovas")
            else:
                print(f"{employee.name} {employee.last_name} - {employee.job_position}")
        print("*" * 80)


def assign_employee_to_department():
    show_employees()
    show_departments()
    
    with session_maker() as session:
        try:
            employee_id = get_int_input("Įveskite darbuotojo ID: ")
            department_id = get_int_input("Įveskite departamento ID: ")
            to_manage = input("Ar darbuotoją norite padaryti departamento vadovu - Parasykite 'taip' arba 't': ").strip().lower()

            employee = session.execute(select(Employee).where(Employee.id == employee_id)).scalar_one_or_none()
            department = session.execute(select(Department).where(Department.id == department_id)).scalar_one_or_none()

            if not employee:
                print(f"Darbuotojas su ID {employee_id} nerastas.")
                return
            
            if not department:
                print(f"Departamentas su ID {department_id} nerastas.")
                return
            
            if employee.department_id == department_id:
                print(f"Darbuotojas jau priskirtas departamentui {department_id}.")
                return

            if to_manage in ("taip", "t"):
                if department.manager_id:
                    print(f"Departamentas jau turi vadovą (ID: {department.manager_id}).")
                    return
                department.manager_id = employee_id

            employee.department_id = department_id
            session.commit()

            print(f"Darbuotojas {employee_id} sėkmingai priskirtas departamentui {department_id}.")

        except Exception as e:
            session.rollback()
            print(f"Klaida priskiriant darbuotoją departamentui: {e}")