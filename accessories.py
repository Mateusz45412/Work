import colorama
from colorama import Fore

line_sn = 5
meters = 1000
number_of_trips = 6

def func_add(l_sn, meter):
    def decorator_error(func_as_param):
        def func_safeguard():
            while True:
                try:
                    func_as_param()  # <-- wywołanie
                    break
                except ValueError:
                    print(Fore.LIGHTRED_EX + "Podaj wartość liczbową!!")
        return func_safeguard()

    def func_cost_project():
        cost_project = int(input(Fore.LIGHTGREEN_EX + "Ile wynosi koszt wykonania projektu ? "))
        return cost_project
    cost_project = func_cost_project()

    @decorator_error
    def func_turn_off():
        turn_off = int(input(Fore.LIGHTGREEN_EX + "ile jest wyłączeń? "))
        return turn_off
    @decorator_error
    def func_cost_petrol():
        cost_petrol = float(input(Fore.LIGHTGREEN_EX + "Ile kosztuje teraz DISEL ? "))
        return cost_petrol
    @decorator_error
    def func_distance():
        distance = float(input(Fore.LIGHTGREEN_EX + "Jak daleko jest budowa ? (podaj w km): "))
        return distance




    def decorator_error2(func_as_param):
        def true_false():
            while True:
                if func_as_param() == True:
                    break
                else:
                    print(Fore.LIGHTRED_EX + "EJJ wpisz -- y -- lub -- n -- ")
        return true_false()

    @decorator_error2
    def mpec():
        collision_mpec = input(Fore.LIGHTGREEN_EX + "Czy wystepuje kolizja z MPEC ? y/n ").lower()
        return False if collision_mpec != "y" and collision_mpec != "n" else True

    @decorator_error2
    def gaz():
        collision_gaz = input(Fore.LIGHTGREEN_EX + "Czy wystepuje kolizja z gazem ? y/n ").lower()
        return False if collision_gaz != "y" and collision_gaz != "n" else True

    @decorator_error2
    def optical():
        collision_optical = input(Fore.LIGHTGREEN_EX + "Czy wystepuje kolizja ze światłowodami ? y/n ").lower()
        return False if collision_optical != "y" and collision_optical != "n" else True

    @decorator_error2
    def PKP():
        collision_PKP = input(Fore.LIGHTGREEN_EX + "Czy wystepuje kolizja z PKP ? y/n ").lower()
        return False if collision_PKP != "y" and collision_PKP != "n" else True

    @decorator_error2
    def river():
        collision_river = input(Fore.LIGHTGREEN_EX + "Czy wystepuje pozwolenie z Wód Polskich ? y/n ").lower()
        return False if collision_river != "y" and collision_river != "n" else True

    COST_MPEC = 1000
    COST_GAZ = 2000
    COST_OPTICAL_FIBER = 500
    COST_ROAD = 1500
    COST_PROJECT_ROAD = 2000
    COST_RIVER = 2000
    COST_PKP = 10000
    kenetration = 1600 + ((l_sn - 1) * 500)
    PREPARE = 2400
    CLEAN = 2400
    CABLE_DELIVERY = 1500
    DOC_COMPLETION = 1000
    MATERIALS_ADD = 10000
    COST_TURN_OFF = 500
    geodesy = (meter * 5)  # dopisz jeszcze za słupy i złącza

    def func_projects(c_project):
        return print(f"Projekt: {c_project} zł") if c_project != 0 else False
    func_projects(cost_project)
    def func_kenetration(lsn):
        return print(f"Kenetracja: {kenetration} zł") if lsn != 0 else False

    def func_mpec(COST, c_mpec):
        return print(f"MPC: {COST} zł") if c_mpec == "y" else False

    def func_gaz(COST, c_gaz):
        return print(f"Gaz: {COST} zł") if c_gaz == "y" else False

    def func_pkp(COST, c_pkp):
        return print(f"PKP: {COST} zł") if c_pkp == "y" else False

    def func_river(COST, c_river):
        return print(f"Wody Polskie: {COST} zł") if c_river == "y" else False

    def func_optical_fiber(COST, c_optical):
        return print(f"Światłowody: {COST} zł") if c_optical == "y" else False

    def func_road_city(COST, c_road_c):
        return print(f"Droga miejska: {COST} zł") if c_road_c == "y" else False

    def func_road_powiat(COST, c_road_p):
        return print(f"Droga powiatowa: {COST} zł") if c_road_p == "y" else False

    def func_project_road(COST, quantity):
        return print(f"Projekt organizacji ruchu: {COST * quantity} zł") if quantity != 0 else False

    def func_turn_off(COST, how_much):
        return print(f"Wyłączenie: {COST * how_much}  ") if turn_off == "y" else False

