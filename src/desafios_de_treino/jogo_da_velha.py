def isRowWinner(field):
    """"linha vencendora"""
    winners = set()

    for i in range(0, 9, 3):
        line = field[i:i+3]
        if line[0] == line[1] == line[2] and line[0] != '.':
            winners.add(line[0])

    if len(winners) == 1:
        return True
    else:
        return False

print(isRowWinner(['X', 'X', 'X', 'O', 'O', '.', '.', '.', '.']))  # True
print(isRowWinner(['X', 'O', 'X', 'O', 'O', 'O', 'X', '.', 'X']))  # True
print(isRowWinner(['X', 'O', '.', '.', 'X', 'O', '.', '.', 'X']))  # False
print(isRowWinner(['X', 'X', 'X', 'O', 'O', 'O', '.', '.', '.']))  # False
