import numpy as np

def first_choice(door, doors, verbose=0):
    while True:
        try: 
            first = int(door)
        except ValueError:
            print(f"'{door}' is not an integer. Try again.")
            continue

        if door in doors:
            break
        else: 
            print(f"Invalid choice: {door}. Please pick 1, 2, or 3")

    #Boolean mask for doors != first_choice, then return those
    remaining_doors = doors[doors != door]
    if verbose == 1:
        print(f"Remaining Doors = {remaining_doors[0]} and {remaining_doors[1]}")

    return remaining_doors


def eliminate_a_loser(options: np.ndarray, winner:int):
    """ 
    options: numpy array of two door numbers (e.g., [1, 3])
    winner: the winning door number
    
    Returns: 
    remaining: numpy array of length 1 (the door left)
    eliminated: the door that was eliminated
    """
    losers = options[options != winner]
    eliminated = np.random.choice(losers)
    remaining = options[options != eliminated]
    return remaining, eliminated
