def is_int_num(num):
    try:
        int(num)
        return True
    except ValueError:
        print(f"{num} is not an integer number. Please enter again!")
        return False


while True:
    k = input("Enter value for k: ")
    if is_int_num(k):
        k = int(k)
        break
while True:
    num_list = input("Enter the element of the list: ").split()
    if all(is_int_num(i) for i in num_list):
        num_list = [(int(i)) for i in num_list]
        break
sub_list = [int(i) for i in num_list]

start_index = list(range(0, len(sub_list) - k + 1))
end_index = list(range(k, len(sub_list) + 1))

result = [max(sub_list[i:j]) for i, j in zip(start_index, end_index)]
print(result)
