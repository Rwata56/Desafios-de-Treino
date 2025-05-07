def max_thrill(A):
    max1 = float('-inf')
    max2 = float('-inf')
    max_thrill = 0

    for j, val in enumerate(A):
        if j > 0:
            max_thrill = max(max_thrill, max1 + val + j)
        if j < len(A) - 1:
            max_thrill = max(max_thrill, max2 + val - j)
        max_thrill = max(max_thrill, 2 * val)
        max1 = max(max1, val - j)
        max2 = max(max2, val + j)

    return max_thrill

A = [1, 3, -2, 4]
print("O valor máximo de thrill é:", max_thrill(A))
