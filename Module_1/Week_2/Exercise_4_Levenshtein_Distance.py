target = input("Enter the target string: ")
source = input("Enter the source string: ")


def edit_distance(tar, src):
    distance = [[0 for i in range(len(src) + 1)] for j in range(len(tar) + 1)]
    for idx in range(len(tar) + 1):
        distance[idx][0] = idx

    for jdx in range(len(src) + 1):
        distance[0][jdx] = jdx

    for idx in range(1, len(tar) + 1):
        for jdx in range(1, len(src) + 1):
            if tar[idx - 1] == src[jdx - 1]:
                distance[idx][jdx] = distance[idx - 1][jdx - 1]
            else:
                distance[idx][jdx] = 1 + min(distance[idx - 1][jdx], distance[idx][jdx - 1], distance[idx - 1][jdx - 1])
    return distance[len(tar)][len(src)]


print(edit_distance(target, source))
