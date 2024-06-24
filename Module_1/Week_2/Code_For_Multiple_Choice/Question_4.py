def levenshtein_distance(token1, token2):
    # Your Code Here
    distance = [[0 for _ in range(len(token2) + 1)] for _ in range(len(token1) + 1)]
    # End Code Here
    for i in range(len(token1) + 1):
        distance[i][0] = i

    for j in range(len(token2) + 1):
        distance[0][j] = j

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1]) + 1
    return float(distance[len(token1)][len(token2)])

def is_close(a, b, rel_tol=1e-9, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

assert is_close(levenshtein_distance("hi", "hello"), 4.0)
print(levenshtein_distance(" hola ", " hello "))
