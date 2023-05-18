

head = int(input("podaj ilosć kpl głowic do wykonania: "))
muff = int(input("podaj ilosć kpl muf do wykonania: "))


def heads(head):
    day_head = head / 2
    cost_head = day_head * 2 * 600
    return print(f"Montaż {head} kpl głowic: {day_head} * 2 prac. * 600 = {cost_head} ") if head!=0 else False


def muffs(muff):
    cost_muf = muff * 2 * 600
    return print(f"Montaż {muff} kpl muf: {muff} * 2 prac. * 600 = {cost_muf} ") if muff != 0 else False

auctions(auction)
muffs(muff)
heads(head)


# connector_sn = int(input("podaj ilość złącz SN do wybudowania "))
# connector_nn = int(input("podaj ilość złącz nN do wybudowania "))

# station_in = int(input("podaj ilosć ST. TR. kontenerowej do postawienia "))
# station_out = int(input("podaj ilosć ST. TR. słupowych do postawienia "))
# pole_sn = int(input("podaj ilosć słupów SN do postawienia "))
# pole_nn = int(input("podaj ilosć słupów nN do postawienia "))

# disassembly_pole_sn = int(input("podaj ilosć słupów SN do demontażu"))
# disassembly_pole_nn = int(input("podaj ilosć słupów nN do demontażu "))
# disassembly_station_out = int(input("podaj ilosć ST. TR. słupowej do demontażu "))



