from movement import find_player_position
from cell import Cell

def check_win(grid, p1_active, p2_active):
    p1_pos = find_player_position(grid, 'p1')
    p2_pos = find_player_position(grid, 'p2')
    t1_pos = find_player_position(grid, 't1')
    t2_pos = find_player_position(grid, 't2')

    if p1_active and t1_pos and p1_pos == t1_pos:
        grid[t1_pos[0]][t1_pos[1]] = Cell('P1')
        p1_active = False
    
    if p2_active and t2_pos and p2_pos == t2_pos:
        grid[t2_pos[0]][t2_pos[1]] = Cell('P2')
        p2_active = False

    return p1_active, p2_active


def check_both_reached_targets(grid):
    p1_pos = find_player_position(grid, 'p1')
    p2_pos = find_player_position(grid, 'p2')
    t1_pos = find_player_position(grid, 't1')
    t2_pos = find_player_position(grid, 't2')
    
    if p1_pos == t1_pos:
        print("Player 1 reached their target (t1)!")

    if p2_pos == t2_pos:
        print("Player 2 reached their target (t2)!")

    if p1_pos == t1_pos and p2_pos == t2_pos:
        print("Both players have reached their targets! Game Over!")
        return True
    
    return False
