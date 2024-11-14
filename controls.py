def get_direction_input():
    direction = input("Enter move (w: up, s: down, a: left, d: right): ").strip().lower()
    if direction == "w":
        return (-1, 0)  
    elif direction == "s":
        return (1, 0)  
    elif direction == "a":
        return (0, -1)  
    elif direction == "d":
        return (0, 1)  
    else:
        print("Invalid input. Try again.")
        return get_direction_input()
