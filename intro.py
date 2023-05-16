number_auction = int(input("podaj nr.przetargu "))
name_auction = input("podaj nazwę przetargu ")
auction = input("czy jest aukcja ? wpisz y/n ")
deposit = int(input("Ile wynosi wadium ? "))
end = input("Wpisz termin końcowy realzacji ")


def func_auctions(auction):
    return print("Aukcja: TAK") if auction=="y" else print("Aukcja: NIE")


def func_security_deposit(deposit):
    return print(f"Wadium: {deposit} zł") if deposit!=0 else print("Wadium: NIE")

print(f"Przetrag nr {number_auction} \n{name_auction}")
print(f"Termin realizacji: {end}")

func_auctions(auction)
func_security_deposit(deposit)