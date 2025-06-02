import heapq
from collections import deque

GOAL_STATE = (1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10, 11, 12,
              13, 14, 15, 0)

MOVES = {
    'UP': -4,
    'DOWN': 4,
    'LEFT': -1,
    'RIGHT': 1,
}

def manhattan_distance(state):
    distance = 0
    for index, value in enumerate(state):
        if value == 0:
            continue
        goal_index = value - 1
        x1, y1 = divmod(index, 4)
        x2, y2 = divmod(goal_index, 4)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)

    x, y = divmod(zero_index, 4)

    for move, delta in MOVES.items():
        new_zero = zero_index + delta
        if move == 'UP' and x == 0:
            continue
        if move == 'DOWN' and x == 3:
            continue
        if move == 'LEFT' and y == 0:
            continue
        if move == 'RIGHT' and y == 3:
            continue

        new_state = list(state)
        new_state[zero_index], new_state[new_zero] = new_state[new_zero], new_state[zero_index]
        neighbors.append((tuple(new_state), move))

    return neighbors

def solve(start_state):
    heap = []
    heapq.heappush(heap, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while heap:
        _, cost_so_far, current_state, path = heapq.heappop(heap)

        if current_state == GOAL_STATE:
            return path

        if current_state in visited:
            continue
        visited.add(current_state)

        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                new_cost = cost_so_far + 1
                estimated_total = new_cost + manhattan_distance(neighbor)
                heapq.heappush(heap, (estimated_total, new_cost, neighbor, path + [move]))

    return None

if __name__ == "__main__":
    start = (15, 14, 1, 6,
              9, 11, 4, 12,
              0, 10, 7, 3,
              13, 8, 5, 2)

    solution = solve(start)

    if solution:
        print(f"Solução encontrada em {len(solution)} movimentos:")
        print(solution)
    else:
        print("Não foi possível encontrar solução.")
