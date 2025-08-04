from typing import List


def next_generation(grid: List[List[int]]) -> List[List[int]]:
    """Calcula a próxima geração no Jogo da Vida de Conway."""
    if not grid:
        return []

    rows: int = len(grid)
    cols: int = len(grid[0]) if rows > 0 else 0

    new_grid: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
    directions: List[tuple[int, int]] = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for i in range(rows):
        for j in range(cols):
            live_neighbors: int = 0

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    live_neighbors += 1

            # Regras atualizadas com condições mais claras
            if grid[i][j] == 1:  # Célula viva
                new_grid[i][j] = 1 if live_neighbors in {2, 3} else 0
            else:  # Célula morta
                new_grid[i][j] = 1 if live_neighbors == 3 else 0

    return new_grid
