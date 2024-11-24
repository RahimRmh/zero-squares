from heapq import heappush, heappop
from win_condition import check_both_reached_targets
from movement import find_player_position , generate_next_states
import copy
from cell import Cell


def ucs_to_win(grid):
    # Priority queue (min-heap)
    priority_queue = []
    visited = set()
    parent_map = {}

    # Start with the initial grid and cost = 0
    start_state = (0, tuple(tuple(cell.cell_type for cell in row) for row in grid), None)  # (cost, grid_tuple, parent)
    heappush(priority_queue, start_state)

    while priority_queue:
        current_cost, grid_tuple, parent = heappop(priority_queue)

        if grid_tuple in visited:
            continue
        visited.add(grid_tuple)
        parent_map[grid_tuple] = (parent, current_cost)

        # Convert tuple back to grid structure for operations
        current_grid = [[Cell(cell_type) for cell_type in row] for row in grid_tuple]

        # Check win condition
        if check_both_reached_targets(current_grid):
            return trace_path_with_cost(parent_map, grid_tuple), current_cost

        # Generate next states for both players
        p1_pos = find_player_position(current_grid, 'p1')
        if p1_pos:
            next_states = generate_next_states(current_grid, p1_pos, 'p1', True, True)
            for next_state in next_states:
                next_tuple = tuple(tuple(cell.cell_type for cell in row) for row in next_state)
                if next_tuple not in visited:
                    heappush(priority_queue, (current_cost + 1, next_tuple, grid_tuple))  # Increment cost by 1

        p2_pos = find_player_position(current_grid, 'p2')
        if p2_pos:
            next_states = generate_next_states(current_grid, p2_pos, 'p2', True, True)
            for next_state in next_states:
                next_tuple = tuple(tuple(cell.cell_type for cell in row) for row in next_state)
                if next_tuple not in visited:
                    heappush(priority_queue, (current_cost + 1, next_tuple, grid_tuple))  # Increment cost by 1

    return None, float('inf')  # Return None if no solution is found



def trace_path_with_cost(parent_map, winning_grid_tuple):
    path = []
    current = winning_grid_tuple

    while current is not None:
        parent, cost = parent_map[current]
        path.append((current, cost))
        current = parent

    path.reverse()  # Return the path from start to goal
    return path
