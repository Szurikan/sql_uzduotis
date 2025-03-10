import datetime

def get_string_input(text):
    while True:
        value = input(text).strip()
        if not value:
            print("Ivestis negali buti tuscia")
            continue
        return value
    
def get_date(text):
    while True:
        birth_date_string = input(text)
        try:
            birth_date = datetime.datetime.strptime(birth_date_string, "%Y-%m-%d")
            break
        except ValueError:
            print("Įvedėte neteisingą formatą. Bandykite dar kartą.")
            continue
    return birth_date
    
def get_int_input(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print("Neteisinga ivestis.")
            continue
    return value