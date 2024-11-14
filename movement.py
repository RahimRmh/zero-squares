from cell import Cell
import copy

def find_player_position(grid, player):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.cell_type == player:
                return (i, j)
    return None

def move_player(grid, direction, p1_active=True, p2_active=True):
    p1_pos = find_player_position(grid, 'p1')
    p2_pos = find_player_position(grid, 'p2')
    dx, dy = direction
    
    if p1_active and p1_pos:
        move_until_block_or_target(grid, p1_pos, dx, dy, 'p1', 'p2', 't1', 't2')
    
    if p2_active and p2_pos:
        move_until_block_or_target(grid, p2_pos, dx, dy, 'p2', 'p1', 't2', 't1')

    return p1_active, p2_active

def move_until_block_or_target(grid, pos, dx, dy, player, opponent, own_target, opponent_target):
    x, y = pos
    new_x, new_y = x + dx, y + dy

    while 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
        if grid[new_x][new_y].cell_type == own_target:
            grid[new_x][new_y] = Cell(player.upper())
            grid[x][y] = Cell('_')
            print(f"{player} reached their target!")
            return False

        if grid[new_x][new_y].cell_type == '*':
            print(f"{player} hit a block!")
            break

        if grid[new_x][new_y].cell_type == opponent_target:
            print(f"{player} hit {opponent}'s target ({opponent_target}) but continues moving...")
            new_x, new_y = new_x + dx, new_y + dy
            continue

        if grid[new_x][new_y].cell_type == opponent:
            print(f"{player} hit {opponent}! Stopping movement.")
            break

        else:
            grid[x][y] = Cell('_')
            grid[new_x][new_y] = Cell(player)

        x, y = new_x, new_y
        new_x, new_y = x + dx, new_y + dy

    return True

def generate_next_states(grid, player_pos, player, p1_active, p2_active):
    next_states = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    original_grid = copy.deepcopy(grid)

    for direction in directions:
        grid = copy.deepcopy(original_grid)
        initial_pos = find_player_position(grid, player)

        if player == 'p1' and p1_active:
            p1_active, p2_active = move_player(grid, direction, p1_active=True, p2_active=False)
        elif player == 'p2' and p2_active:
            p1_active, p2_active = move_player(grid, direction, p1_active=False, p2_active=True)

        new_pos = find_player_position(grid, player)

        if initial_pos != new_pos:
            next_states.append(copy.deepcopy(grid))

    return next_states
