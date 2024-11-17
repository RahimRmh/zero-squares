from movement import generate_next_states, find_player_position
from win_condition import check_both_reached_targets
import copy

def dfs_to_win(grid):
    stack = [(copy.deepcopy(grid), None)]
    visited = set()
    parent_map = {}

    while stack:
        current_grid, parent = stack.pop()
        grid_tuple = tuple(tuple(cell.cell_type for cell in row) for row in current_grid)
        
        if grid_tuple in visited:
            continue
        visited.add(grid_tuple)
        parent_map[grid_tuple] = parent

        if check_both_reached_targets(current_grid):
            return trace_path(parent_map, grid_tuple)

        p1_pos = find_player_position(current_grid, 'p1')
        if p1_pos:
            next_states = generate_next_states(current_grid, p1_pos, 'p1', True, True)
            for next_state in next_states:
                next_tuple = tuple(tuple(cell.cell_type for cell in row) for row in next_state)
                if next_tuple not in visited:
                    stack.append((next_state, grid_tuple))

        p2_pos = find_player_position(current_grid, 'p2')
        if p2_pos:
            next_states = generate_next_states(current_grid, p2_pos, 'p2', True, True)
            for next_state in next_states:
                next_tuple = tuple(tuple(cell.cell_type for cell in row) for row in next_state)
                if next_tuple not in visited:
                    stack.append((next_state, grid_tuple))

    return None

def trace_path(parent_map, winning_grid_tuple):
    path = []
    current = winning_grid_tuple
    while current is not None:
        path.append(current)
        current = parent_map[current]
    return list(reversed(path))
