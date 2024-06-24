import math


def is_number(n):
    try:
        return float(n)  # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return None


def get_valid_number():
    num_input = is_number(input(">> Input x = "))
    if num_input is None:
        print("x must be a number")
        return get_valid_number()
    return num_input


def get_valid_activation_function():
    func = input("Input activation Function (sigmoid|relu|elu): ")
    if func not in ["sigmoid", "relu", "elu"]:
        print(f"{func} is not supported")
        return get_valid_activation_function()
    return func


x = get_valid_number()
activate_func = get_valid_activation_function()

if activate_func == "sigmoid":
    print(f"sigmoid: f({x}) = ", 1 / (1 + math.pow(math.e, -x)))
elif activate_func == "relu":
    print(f"relu: f({x}) = ", max(0, x))
elif activate_func == "elu":
    print(f"elu: f({x}) = ", x if x > 0 else 0.01 * (math.pow(math.e, x) - 1))
