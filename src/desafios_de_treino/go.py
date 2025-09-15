from typing import Dict, Set, Tuple, List


BLACK = 'B'
WHITE = 'W'
NONE = ' '


class Board:
    def __init__(self, board: List[str]):
        self.board = [list(row) for row in board]
        self.rows = len(board)
        self.cols = len(board[0]) if board else 0

    def is_valid(self, x: int, y: int) -> bool:
        """Check if coordinates are within board bounds."""
        return 0 <= y < self.rows and 0 <= x < self.cols

    def territory(self, x: int, y: int) -> Tuple[str, Set[Tuple[int, int]]]:
        """Find the territory and its owner for a given coordinate."""
        if not self.is_valid(x, y):
            raise ValueError("Invalid coordinate")

        # If the coordinate contains a stone, it's not a territory
        if self.board[y][x] != ' ':
            return NONE, set()

        visited = set()
        territory = set()
        borders = set()
        stack = [(x, y)]

        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue

            visited.add((cx, cy))
            territory.add((cx, cy))

            # Check all four directions
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = cx + dx, cy + dy
                if self.is_valid(nx, ny):
                    cell = self.board[ny][nx]
                    if cell == ' ':
                        if (nx, ny) not in visited:
                            stack.append((nx, ny))
                    else:
                        borders.add(cell)
                # If we're at the edge of the board, it's a border
                else:
                    borders.add(NONE)

        # Determine owner based on borders
        if BLACK in borders and WHITE in borders:
            owner = NONE
        elif BLACK in borders:
            owner = BLACK
        elif WHITE in borders:
            owner = WHITE
        else:
            owner = NONE

        return owner, territory

    def territories(self) -> Dict[str, Set[Tuple[int, int]]]:
        """Find all territories on the board."""
        all_territories = {BLACK: set(), WHITE: set(), NONE: set()}
        visited = set()

        for y in range(self.rows):
            for x in range(self.cols):
                if self.board[y][x] == ' ' and (x, y) not in visited:
                    owner, territory = self.territory(x, y)
                    all_territories[owner].update(territory)
                    visited.update(territory)

        return all_territories