def sum_of_diagonals(n):
    total_sum = 1
    current_number = 1


    for layer in range(1, (n // 2) + 1):
        step = layer * 2
        for i in range(4):
            current_number += step
            # print (f"{current_number}-{"numero atual"}")
            total_sum += current_number
            # print (f"{total_sum}-{"numero somado"}")

    return total_sum

result = sum_of_diagonals(1001)
print(result)
