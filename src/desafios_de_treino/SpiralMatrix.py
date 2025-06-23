def generate_spiral_matrix(n: int) -> list[list[int]]:
    if not n :
        return []

    matrix = [[0] * n for _ in range(n)]
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1
    current_num = 1

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = current_num
            current_num += 1
        start_row += 1

        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = current_num
            current_num += 1
        end_col -= 1

        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                matrix[end_row][i] = current_num
                current_num += 1
            end_row -= 1

        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                matrix[i][start_col] = current_num
                current_num += 1
            start_col += 1

    return matrix