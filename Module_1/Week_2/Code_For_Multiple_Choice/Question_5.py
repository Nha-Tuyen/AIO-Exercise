def check_the_number(n):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Your code here
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)

    if n in list_of_numbers:
        result = " True "
    if n not in list_of_numbers:
        result = " False "
    return result


N = 7
assert check_the_number(N) == " False "
N = 2
results = check_the_number(N)
print(results)
