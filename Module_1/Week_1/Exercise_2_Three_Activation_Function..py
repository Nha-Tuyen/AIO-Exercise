import math


def is_number(n):
    try:
        return float(n)  # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return None


while True:
    x = is_number(input(">> Input x = "))
    if x is None:
        print("x must be a number")
        continue
    break
while True:
    activate_func = input("Input activation Function (sigmoid|relu|elu): ")
    if activate_func not in ["sigmoid", "relu", "elu"]:
        print(f"{activate_func} is not supported")
    else:
        if activate_func == "sigmoid":
            print(f"sigmoid: f({x}) = ", 1 / (1 + math.pow(math.e, -x)))
        elif activate_func == "relu":
            print(f"relu: f({x}) = ", max(0, x))
        elif activate_func == "elu":
            print(f"elu: f({x}) = ", x if x > 0 else 0.01 * (math.pow(math.e, x) - 1))
        break
