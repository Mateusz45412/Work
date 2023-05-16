def decorator_error2(func_as_param):
    def true_false():
        while True:
            if func_as_param() == True:
                print("jest ok")
                break
            else:
                print("EJJ wpisz -- y -- lub -- n -- ")
    return true_false()
#
@decorator_error2
def mpec():
    func = input("Czy wystepuje kolizja z MPEC ? y/n ").lower()
    return False if func != "y" and func != "n" else True

# mpec()

# while True:
#     func_as_param = input("Czy wystepuje kolizja z MPEC ? y/n ").lower()
#     if func_as_param == "y" or func_as_param == "n":
#         print("jest ok")
#         break
#     else:
#         print("EJJ wpisz -- y -- lub -- n -- ")




