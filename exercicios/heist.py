def maximumThrill(atms):
    max_thrill = 0
    best_i = best_j = -1

    for i in range(len(atms)):
        for j in range(i, len(atms)):
            thrill = atms[i] + atms[j] + abs(i - j)
            if thrill > max_thrill:
                max_thrill = thrill
                best_i, best_j = i, j

    print(f"Melhor par de índices: ({best_i}, {best_j}) -> valores: ({atms[best_i]}, {atms[best_j]})")
    return max_thrill

print(maximumThrill([3, 1, 3]))
print(maximumThrill([2, 3, 4, 5]))
print(maximumThrill([10, 10, 11, 13, 7, 8, 9]))
