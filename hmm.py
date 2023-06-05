import colorama
line_sn = 5
meters = 1000
number_of_trips = 6
##########
def decorator_error(func_as_param):
    def func_safeguard():
        while True:
            try:
                func_as_param()  # <-- wywołanie
                break
            except ValueError:
                print("Podaj wartość liczbową!!")
    return func_safeguard()

def cost():
    cost_project = int(input("Ile wynosi koszt wykonania projektu ? "))


def func_add(l_sn, meter):

    while True:
        try:
            cost_project = int(input("Ile wynosi koszt wykonania projektu ? "))
            break
        except ValueError:
            print("Podaj wartość liczbową (!!")

    while True:
        try:
            turn_off = int(input("ile jest wyłączeń? "))
            break
        except ValueError:
            print("Podaj wartość liczbową !!")

    while True:
        try:
            cost_petrol = float(input("Ile kosztuje teraz DISEL ? "))
            break
        except ValueError:
            print("Podaj wartość liczbową (!!")

    while True:
        try:
            distance = float(input("Jak daleko jest budowa ? (podaj w km): "))
            break
        except ValueError:
            print("Podaj wartość liczbową !!")

    collision_mpec = input("Czy wystepuje kolizja z MPEC ? y/n ").lower()
    collision_gaz = input("Czy wystepuje kolizja z gazem ? y/n ").lower()
    collision_optical = input("Czy wystepuje kolizja ze światłowodami ? y/n ").lower()
    collision_PKP = input("Czy wystepuje kolizja z PKP ? y/n ").lower()
    collision_river = input("Czy wystepuje pozwolenie z Wód Polskich ? y/n ").lower()
    collision_road = input("Czy występują kolizje z drogami ? y/n ").lower()
    if collision_road == "y":
        collision_road_city = input("Czy jest to droga miejska? y/n ").lower()
        collision_road_powiat = input("Czy jest to droga powiatowa? y/n ").lower()
        collision_project_road = int(input("Ile potrzebujesz projektów organizacji ruchu? y/n ").lower())
    else:
        collision_road_city = "n"
        collision_road_powiat = "n"
        collision_project_road = 0
        pass

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

    func_projects(cost_project)
    func_turn_off(COST_TURN_OFF, turn_off)
    func_kenetration(l_sn)
    func_mpec(COST_MPEC, collision_mpec)
    func_gaz(COST_GAZ, collision_gaz)
    func_pkp(COST_PKP, collision_PKP)
    func_river(COST_RIVER, collision_river)
    func_optical_fiber(COST_OPTICAL_FIBER, collision_optical)
    func_road_city(COST_ROAD, collision_road_city)
    func_road_powiat(COST_ROAD, collision_road_powiat)
    func_project_road(COST_PROJECT_ROAD, collision_project_road)

    print(f"Paliwo: {(((10 * cost_petrol) * distance) * number_of_trips) * 2}")
    print(f"Geodezja: {geodesy} zł")
    print(f"Dostawa kabla: {CABLE_DELIVERY} zł")
    print(f"Dokumentacja powykonawcza: {DOC_COMPLETION} zł")
    print(f"Materiały dodatkowe: {MATERIALS_ADD} zł")
    print(f"Przygotowanie: {PREPARE} zł \nSprzątanie: {CLEAN} zł")


func_add(line_sn, meters)
