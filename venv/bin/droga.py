def road():
    while True:
        collision_road = input("Czy występują kolizje z drogami ? y/n ")
        if collision_road in "y":
            while True:
                collision_road_city = input("Czy jest to droga miejska? ")
                if not collision_road_city in "y" and not collision_road_city in "n":
                    print("EJJ wpisz -- y -- lub -- n -- ")
                elif collision_road_city in "n":
                    break

            while True:
                collision_road_powiat = input("Czy jest to droga powiatowa? ")
                if not collision_road_powiat in "y" and collision_road_powiat in "n":
                    print("EJJ wpisz -- y -- lub -- n -- ")
                elif collision_road_powiat in "n":
                    break
            # while True:
            #     try:
            #         collision_project_road = int(input("Ile potrzebujesz projektów organizacji ruchu? "))
            #         break
            #     except ValueError:
            #         print("Podaj wartość liczbową!!")

                COST_ROAD = 1500
                COST_PROJECT_ROAD = 2000

                def func_road_city(COST, c_road_c):
                    return print(f"Droga miejska: {COST} zł") if c_road_c in "y" else False

                def func_road_powiat(COST, c_road_p):
                    return print(f"Droga powiatowa: {COST} zł") if c_road_p in "y" else False

                # def func_project_road(COST, quantity):
                #     return print(f"Projekt organizacji ruchu: {COST * quantity} zł") if quantity != 0 else False

                func_road_city(COST_ROAD, collision_road_city)
                func_road_powiat(COST_ROAD, collision_road_powiat)
                # func_project_road(COST_PROJECT_ROAD, collision_project_road)
            break
        elif collision_road in "n":
            break

        elif not collision_road in "y" or "n":
            print("EJJ wpisz -- y -- lub -- n -- ")

road()




