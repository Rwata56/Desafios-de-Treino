def annotate(board):
    if not board:
        return []

    rows = len(board)
    cols = len(board[0])
    result = []

    for i in range(rows):
        new_row = ''
        for j in range(cols):
            if board[i][j] == '*':
                new_row += '*'
            else:
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if board[ni][nj] == '*':
                                count += 1
                new_row += str(count) if count > 0 else '0'
        result.append(new_row)
    return result

board = [
    ' * * ',
    '  *  ',
    '  *  ',
    '     '
]

saida = annotate(board)

for linha in saida:
    print(linha)
