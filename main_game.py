from grid_history import initialize_grid_history, store_grid_in_history, print_grid_history
from movement import move_player, generate_next_states, find_player_position
from win_condition import check_win, check_both_reached_targets
from controls import get_direction_input
from cell import Cell
import copy

grid_history = initialize_grid_history()

grid = [
    [Cell(' '), Cell(' '), Cell(' '), Cell(' '), Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*')],
    [Cell(' '), Cell(' '), Cell(' '), Cell(' '), Cell('*'), Cell('_'), Cell('_'), Cell('_'), Cell('*')],
    [Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('t1'), Cell('*'), Cell('_'), Cell('*')],
    [Cell('*'), Cell('_'), Cell('_'), Cell('_'), Cell('p1'), Cell('_'), Cell('*'), Cell('_'), Cell('*')],
    [Cell('*'), Cell('_'), Cell('_'), Cell('t2'), Cell('*'), Cell('p2'), Cell('*'), Cell('_'), Cell('*')],
    [Cell('*'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('*')],
    [Cell('*'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('_'), Cell('*')],
    [Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*'), Cell('*')],
]

def play_game(grid):
    p1_active, p2_active = True, True

    store_grid_in_history(grid_history, copy.deepcopy(grid))

    while True:
        for row in grid:
            print(' '.join(str(cell) for cell in row))

        p1_pos = find_player_position(grid, 'p1')
        p2_pos = find_player_position(grid, 'p2')

        if p1_active:
            p1_next_states = generate_next_states(grid, p1_pos, 'p1', p1_active=True, p2_active=True)
            for idx, state in enumerate(p1_next_states):
                print(f"Option {idx+1}:")
                for row in state:
                    print(' '.join(str(cell) for cell in row))
                print("---")

        if p2_active:
            p2_next_states = generate_next_states(grid, p2_pos, 'p2', p1_active=True, p2_active=True)
            for idx, state in enumerate(p2_next_states):
                print(f"Option {idx+1}:")
                for row in state:
                    print(' '.join(str(cell) for cell in row))
                print("---")

        direction = get_direction_input()

        move_player(grid, direction, p1_active, p2_active)

        p1_active, p2_active = check_win(grid, p1_active, p2_active)

        store_grid_in_history(grid_history, copy.deepcopy(grid))

        if not check_both_reached_targets(grid):
            print("Both players have reached their targets! Game Over!")
            break

    print("\nGrid History:")
    print_grid_history(grid_history)

play_game(grid)
