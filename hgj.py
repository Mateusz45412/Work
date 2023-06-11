def decorator_error(func_as_param):
    def func_safeguard():
        while True:
            try:###
                func_as_param()  # <-- wywołanie
                break
            except ValueError:
                print("Podaj wartość liczbową!!")
    return func_safeguard()
@decorator_error
def cost():
    cost_project = int(input("Ile wynosi koszt wykonania projektu ? "))

cost()