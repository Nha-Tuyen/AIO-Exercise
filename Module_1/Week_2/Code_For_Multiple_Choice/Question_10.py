def My_function(integers, number=1):
    # for i in integers:
    #     if i == number:
    #         return True
    #     else:
    #         return False
    return any(x == number for x in integers)


my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))
