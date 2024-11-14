
def initialize_grid_history():
    return []

def store_grid_in_history(history, grid):
    history.append(grid)

def print_grid_history(history):
    for i, grid in enumerate(history):
        print(f"Grid State {i + 1}:")
        for row in grid:
            print(' '.join(str(cell) for cell in row))
        print()
