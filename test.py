import colorama
from colorama import Fore

line_sn = 5
meters = 1000
number_of_trips = 6
###

def cost_project():
    cost_project = int(input(Fore.LIGHTGREEN_EX + "Ile wynosi koszt wykonania projektu ? "))
    return cost_project

def func_projects(c_project):
    return print(f"Projekt: {c_project} zł") if c_project != 0 else False

func_projects(cost_project())
