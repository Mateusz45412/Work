def lines():
    sn = input("czy występuje linia kablowa SN ? wpisz y/n ")
    if sn == "y":
        line_sn = int(input("ile jest linii kalowych SN ?"))
        dig_sn = int(input("podaj długość wykopu linii kablowej SN [m] "))
        drill_sn = int(input("podaj długość przewiertu w linii kablowej SN [m] "))
        arrangement_sn = int(input("podaj długość układania kabla w części wykopanej SN "))

        value_dig_sn = dig_sn * 50
        value_drill_sn = drill_sn * 200
        value_arrangement_sn = arrangement_sn * 20
        optical_fiber = (dig_sn + arrangement_sn + drill_sn) * 2 * 10
    else:
        pass

    nn = input("czy występuje linia kablowa nN ? wpisz y/n ")
    if nn == "y":
        dig_nn = int(input("podaj długość wykopu linii kablowej nN [m] "))
        drill_nn = int(input("podaj długość przewiertu w linii kablowej nN [m] "))
        arrangement_nn = int(input("podaj długość układania kabla w części wykopanej nN "))

        value_dig_nn = dig_nn * 50
        value_drill_nn = drill_nn * 200
        value_arrangement_nn = arrangement_nn * 20
    else:
        pass
    meters = dig_sn + drill_sn + arrangement_sn + dig_nn + drill_nn + arrangement_nn

    print(f"kopanie SN: {dig_sn} * 50 = {value_dig_sn}")
    print(f"przewiert SN: {drill_sn} * 200 = {value_drill_sn}")
    print(f"układanie kabla SN (część wykopana): {arrangement_sn} * 20 = {value_arrangement_sn }")
    print(f"układanie rurki światłowodowej: {(dig_sn + arrangement_sn + drill_sn)} * 2 * 10 = {optical_fiber }")

    print(f"kopanie nN: {dig_nn} * 50 = {value_dig_nn}")
    print(f"przewiert nN: {drill_nn} * 200 = {value_drill_nn}")
    print(f"układanie kabla nN (część wykopana): {arrangement_nn} * 20 = {value_arrangement_nn }")
    print(meters)
    return meters
lines()
