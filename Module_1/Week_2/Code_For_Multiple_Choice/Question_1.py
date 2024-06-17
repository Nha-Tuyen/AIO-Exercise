def max_kernel(num_list, k):
    result = []

    # Your Code Here
    sub_list = [int(i) for i in num_list]
    start_index = list(range(0, len(sub_list) - k + 1))
    end_index = list(range(k, len(sub_list) + 1))

    # End Code Here
    result = [max(sub_list[i:j]) for i, j in zip(start_index, end_index)]
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
