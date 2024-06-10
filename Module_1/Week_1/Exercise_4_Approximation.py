def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def approx_sin(x, n):
    print(f"approx_sin(x={x}, n={n})")
    sum = 0
    for i in range(n):
        sum += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return print(f">> {sum}\n")


def approx_cos(x, n):
    print(f"approx_cos(x={x}, n={n})")
    sum = 0
    for i in range(n):
        sum += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return print(f">> {sum}\n")


def approx_sinh(x, n):
    print(f"approx_sinh(x={x}, n={n})")
    sum = 0
    for i in range(n):
        sum += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return print(f">> {sum}\n")


def approx_cosh(x, n):
    print(f"approx_cosh(x={x}, n={n})")
    sum = 0
    for i in range(n):
        sum += (x ** (2 * i)) / factorial(2 * i)
    return print(f">> {sum}\n")


print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))
