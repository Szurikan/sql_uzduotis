from models.projects import Project
from database.config import session_maker
from services.app_service import get_string_input, get_int_input
from models.employees import Employee
from models.employee_project import EmployeeProject
from sqlalchemy import select, or_, cast, String


def add_project():
    name = get_string_input("Irasykite projekto pavadinima: ")
    description = get_string_input("Irasykite projekto aprasyma: ")
    with session_maker() as session: # is gamyklos sukuriam automobili kuri naudosime
        project = Project(
            name=name,
            description=description,
            )
        session.add(project)
        session.commit()
    print("Darbuotojas sekmingai pridetas.")

def show_projects():
    with session_maker() as session:
        query = select(Project) # gauname objektus
        projects = session.execute(query).scalars().all()
    if projects:
        print(f"Projektu sarasas: \n")
    for project in projects:
        print(project)
    if not projects:
        print("Projektu nerasta.")

    
def show_employee_projects():
    show_projects()
    with session_maker() as session:
        employee_id = get_int_input("Iveskite darbuotojo ID: ")

        employee = session.get(Employee,employee_id)
        if not employee:
            print("Darbuotojas nerastas")
            return
        
        projects = session.query(Project).join(EmployeeProject).filter(EmployeeProject.employee_id == employee_id).all()

        if not projects:
            print("Darbuotojas nepriskirtas prie projektu.")
            return
        
        print("Darbutojo projektai:")
        for project in projects:
            print(f"- {project.name}: {project.description}")
