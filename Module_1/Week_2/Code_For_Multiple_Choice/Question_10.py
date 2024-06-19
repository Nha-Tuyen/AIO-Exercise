def my_function(integers, number=1):
    #     if i == number:
    #         return True
    #     else:
    #         return False
    return any(x == number for x in integers)


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
