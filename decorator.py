def decorator_error(func_as_param):
    def func_safeguard():
        while True:
            try:
                func_as_param()/2 # <-- wywołanie
                break
            except TypeError:
                print("Podaj wartość liczbową!!")
    return func_safeguard()


@decorator_error
def cost_project():
    cost_project = input("Ile wynosi koszt wykonania projektu ? ")
