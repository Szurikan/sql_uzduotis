from models.employees import Employee
from database.config import session_maker
from services.app_service import get_string_input, get_int_input, get_date
from sqlalchemy import select, or_, cast, String



def add_employee():
    name = get_string_input("Irasykite varda: ")
    last_name = get_string_input("Irasykite pavarde: ")
    birth_date = get_date("Irasykite gimimo data: ")
    job_position = get_string_input("Irasykite pareigas: ")
    salary = get_int_input("Irasykite atlyginima: ")
    with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
        employee = Employee(
            name=name,
            last_name=last_name,
            birth_date=birth_date, 
            job_position=job_position,
            salary=salary
            )
        session.add(employee)
        session.commit()
    print("Darbuotojas pridetas.")

def show_employees():
    with session_maker() as session:
        query = select(Employee) # gauname objektus
        employees = session.query(Employee).all()
        if employees:
            print(f"Darbuotoju sarasas: \n")
        for employee in employees:
            print(employee)
        if not employees:
            print("Darbuotoju nerasta.")
        print("*" * 80)


def search_employee():
    search_term = get_string_input("Įveskite paieškos terminą (vardas, pavardė, gimimo data YYYY-MM-DD, pareigos arba atlyginimas): ").strip()

    with session_maker() as session:
        query = select(Employee).where(
            or_(
                Employee.name.ilike(f"%{search_term}%"),
                Employee.last_name.ilike(f"%{search_term}%"),
                Employee.job_position.ilike(f"%{search_term}%"),
                cast(Employee.birth_date, String).ilike(f"%{search_term}%"),
                cast(Employee.salary, String).ilike(f"%{search_term}%")
            )
        )
        
        employees = session.execute(query).scalars().all()

        if employees:
            print("\nRasti darbuotojai:")
            for employee in employees:
                print(employee)
        else:
            print("Darbuotojų pagal šią paiešką nerasta.")

def update_employee():
    show_employees()
    with session_maker() as session:
        search_id = get_int_input("Iveskite darbuotojo ID: ")
        employee = session.get(Employee,search_id)

        if not employee:
            print("Darbuotojas nerastas")
            return
        
        print("\nKą norite atnaujinti?")
        print("1. Pavardę")
        print("2. Pareigas")
        print("3. Atlyginimą")
        print("4. Grizti i pagrindini meniu")


        choice = input("Pasirinkite numerį: ").strip()

        match choice:
            case "1":
                new_value = get_string_input("Įveskite naują pavardę: ")
                employee.last_name = new_value
            case "2":
                new_value = get_string_input("Įveskite naujas pareigas: ")
                employee.job_position = new_value
            case "3":
                new_value = get_date("Įveskite nauja atlyginima: ")
                employee.salary = new_value
            case "4":
                pass
            case _:
                print("Neteisingas pasirinkimas.")
                return
        
        session.commit()
        print("Darbuotojo informacija atnaujinta.")

def delete_employee():
    
    show_employees()
    with session_maker() as session:
        search_id = get_int_input("Iveskite darbuotojo ID, kuri norite istrinti: ")
        employee = session.get(Employee,search_id)

        if not employee:
            print("Darbuotojas nerastas")
            return
        
        session.delete(employee)
        session.commit()
        print("Darbuotojas istrintas.")
        


# def assign_employee_to_department():
#     show_employees()
#     show_departments()
#     with session_maker() as session:
#         employee_id = get_int_input("Įveskite darbuotojo ID: ")
#         department_id = get_int_input("Įveskite departamento ID: ")

#         employee = session.get(Employee, employee_id)
#         if not employee:
#             print("Darbuotojas nerastas.")
#             return

#         department = session.get(Department, department_id)
#         if not department:
#             print("Departamentas nerastas.")
#             return

#         employee.department_id = department_id
#         session.commit()

#         print("Darbuotojas priskirtas departamentui.")



