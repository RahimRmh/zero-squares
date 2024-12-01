from heapq import heappop, heappush
import copy
from movement import generate_next_states, find_player_position
from win_condition import check_both_reached_targets
from movement import move_player
from cell import Cell

def astar_to_win(grid):
   
    start_state = copy.deepcopy(grid)
    start_tuple = tuple(tuple(cell.cell_type for cell in row) for row in start_state)
    start_cost = 0

    pq = []
    heappush(pq, (start_cost, 0, start_tuple, None))

    visited = set()
    parent_map = {}

    while pq:
        _, path_cost, current_grid_tuple, parent = heappop(pq)

        if current_grid_tuple in visited:
            continue

        visited.add(current_grid_tuple)
        parent_map[current_grid_tuple] = parent

        current_grid = [
            [Cell(cell) for cell in row]
            for row in current_grid_tuple
        ]

        if check_both_reached_targets(current_grid):
            return trace_path_with_cost(parent_map, current_grid_tuple, path_cost)

        p1_pos = find_player_position(current_grid, 'p1')
        p2_pos = find_player_position(current_grid, 'p2')
        t1_pos = find_player_position(current_grid, 't1')
        t2_pos = find_player_position(current_grid, 't2')

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_grid = copy.deepcopy(current_grid)
            move_player(next_grid, direction, p1_active=True, p2_active=True)
            next_tuple = tuple(tuple(cell.cell_type for cell in row) for row in next_grid)

            if next_tuple not in visited:
                g_cost = path_cost + 1  
                h_cost = heuristic(find_player_position(next_grid, 'p1'), t1_pos) + \
                         heuristic(find_player_position(next_grid, 'p2'), t2_pos)
                f_cost = g_cost + h_cost

                heappush(pq, (f_cost, g_cost, next_tuple, current_grid_tuple))

    return None  

def trace_path_with_cost(parent_map, winning_grid_tuple, total_cost):
   
    path = []
    current = winning_grid_tuple
    while current is not None:
        path.append(current)
        current = parent_map[current]
    return list(reversed(path)), total_cost


def heuristic(player_pos, target_pos):
    if player_pos and target_pos:
        return abs(player_pos[0] - target_pos[0]) + abs(player_pos[1] - target_pos[1])
    return float('inf') 