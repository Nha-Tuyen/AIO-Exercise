def my_function(n):
    # Your code here
    min_value = min(n)
    return min_value


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))
