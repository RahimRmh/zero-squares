from grid_history import initialize_grid_history, store_grid_in_history, print_grid_history
from movement import move_player, generate_next_states, find_player_position
from win_condition import check_win, check_both_reached_targets
from controls import get_direction_input
from cell import Cell
from bfs import bfs_to_win
from dfs import dfs_to_win
from ucs import ucs_to_win
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

def display_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

def play_game(grid, search_algorithm):
    if search_algorithm == "bfs":
        winning_path = bfs_to_win(grid)
    elif search_algorithm == "dfs":
        winning_path = dfs_to_win(grid)
    elif search_algorithm == "ucs":
        winning_path, total_cost = ucs_to_win(grid)
        print(f"Total Cost: {total_cost}")
    else:
        print("Invalid search algorithm.")
        return

    if winning_path:
        print("\nWinning Path:")
        for i, (grid_state, cost) in enumerate(winning_path):
            print(f"Step {i + 1} (Cost: {cost}):")
            display_grid(grid_state)
    else:
        print("No winning path possible.")




def interactive_game(grid):
    p1_active, p2_active = True, True
    store_grid_in_history(grid_history, copy.deepcopy(grid))

    while True:
        print("Current Grid:")
        display_grid(grid)

        if check_both_reached_targets(grid):
            print("Both players have reached their targets! Game Over!")
            break

        p1_pos = find_player_position(grid, 'p1')
        p2_pos = find_player_position(grid, 'p2')

        if p1_active:
            print("\nPlayer 1 (p1) Options:")
            p1_next_states = generate_next_states(grid, p1_pos, 'p1', p1_active=True, p2_active=True)
            for idx, state in enumerate(p1_next_states):
                print(f"Option {idx + 1}:")
                display_grid(state)

        if p2_active:
            print("\nPlayer 2 (p2) Options:")
            p2_next_states = generate_next_states(grid, p2_pos, 'p2', p1_active=True, p2_active=True)
            for idx, state in enumerate(p2_next_states):
                print(f"Option {idx + 1}:")
                display_grid(state)

        print("\nEnter move direction for Player 1 and Player 2 (e.g., 'up down'): ")
        direction = get_direction_input()

        move_player(grid, direction, p1_active=True, p2_active=True)  

        p1_active, p2_active = check_win(grid, p1_active, p2_active)

        store_grid_in_history(grid_history, copy.deepcopy(grid))

    print("\nGrid History:")
    print_grid_history(grid_history)

def main():
    print("Choose mode:")
    print("1. Automatic Solution (BFS)")
    print("2. Automatic Solution (DFS)")
    print("3. Automatic Solution (UCS)")
    print("4. Interactive Play")

    mode = input("Enter 1, 2, 3, or 4: ").strip()
    if mode == "1":
        play_game(grid, "bfs")
    elif mode == "2":
        play_game(grid, "dfs")
    elif mode == "3":
        play_game(grid, "ucs")
    elif mode == "4":
        interactive_game(grid)
    else:
        print("Invalid choice. Exiting.")




if __name__ == "__main__":
    main()
