def update_minesweeper_board(board):
    rows = len(board)
    cols = len(board[0])

    # Directions for all 8 neighbors (vertical, horizontal, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]

    # Function to count adjacent mines
    def count_adjacent_mines(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] == '*':
                    count += 1
        return count

    # Create the new board
    new_board = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            if board[r][c] == '*':
                new_row.append('*')
            else:
                count = count_adjacent_mines(r, c)
                new_row.append(str(count) if count > 0 else '0')
        new_board.append(new_row)

    return new_board


# Original board
original_board = [
    [' ', '*', ' ', '*', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

# Update the board
updated_board = update_minesweeper_board(original_board)

# Print the result
for row in updated_board:
    print(''.join(row))



