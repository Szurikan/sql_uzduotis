import os
from colorama import Fore, Style
from services.employee_service import add_employee, show_employees, search_employee, update_employee, delete_employee
from services.project_service import add_project, show_employee_projects, assign_employee_to_project
from services.department_service import add_department, show_department_employees, assign_employee_to_department

def show_menu():
        
    print("Rodomas meniu")
    while True:
        os.system("cls")
        print(Fore.YELLOW +
            "\nMENIU:\n" +
            Fore.CYAN + "1. Pridėti naują darbuotoją\n"
            "2. Atvaizduoti visų darbuotojų sąrašą\n"
            "3. Ieškoti darbuotojo\n"
            "4. Atnaujinti darbuotojo informaciją\n"
            "5. Ištrinti darbuotoją\n"
            "6. Pridėti naują projektą\n"
            "7. Priskirti darbuotoją projektui\n"
            "8. Peržiūrėti darbuotojo projektus\n"
            "9. Sukurti naują departamentą\n"
            "10. Priskirti darbuotoją departamentui\n"
            "11. Peržiūrėti departamento darbuotojus\n"
            "12. Išeiti iš programos" + Style.RESET_ALL
        )
        
        choice = input("Įveskite veiksmo numerį: ").strip()

        match choice:
            case "1":
                add_employee()
            case "2":  
                show_employees()
            case "3":
                search_employee()
            case "4":
                update_employee()
            case "5":
                delete_employee()
            case "6":
                add_project()
            case "7":
                assign_employee_to_project()
            case "8":
                show_employee_projects()
            case "9":
                add_department()
            case "10":
                assign_employee_to_department()
            case "11":
                show_department_employees()
            case "12":
                print("Ačiū. Viso gero.")
                break
            case _:
                print(Fore.RED + "Neteisingas pasirinkimas, bandykite dar kartą." + Style.RESET_ALL)

        input("\nSpauskite Enter, jeigu norite tęsti.")

# initialize_database()
show_menu()