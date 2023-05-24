import colorama
from colorama import Fore

line_sn = 5


def decorator_error(func_as_param):
    def func_safeguard():
        while True:
            try:
                func_as_param()  # <-- wywołanie
                break
            except ValueError:
                print(Fore.LIGHTRED_EX + "Podaj wartość liczbową!!")

    return func_safeguard()
@decorator_error
def func_cost_project():
    cost_project = int(input(Fore.LIGHTGREEN_EX + "Ile wynosi koszt wykonania projektu ? "))
    return cost_project
##

cost_project = func_cost_project()


cabel1 = ((line_sn-1)//3)+1
cabel2 = line_sn-cabel1
kenetration = (cabel1*1700)+(cabel2*500)


# geodesy = (meter * 5)  # dopisz jeszcze za słupy i złącza

def func_projects(c_project):
    return print(f"Projekt: {c_project} zł") if c_project != 0 else False


def func_kenetration(lsn):
    return print(f"Kenetracja: {kenetration} zł") if lsn != 0 else False




func_projects(cost_project)
func_kenetration(kenetration)

