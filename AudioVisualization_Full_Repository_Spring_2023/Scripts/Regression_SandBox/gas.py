import random

def generate_array_size():
    """
    Generate a random integer between 4 and 10000 that is a good size for an array.

    Returns:
        int: A random integer between 4 and 10000.
    """
    # Choose a base size between 100 and 1000
    base_size = random.randint(100, 1000)

    # Choose a multiplier between 1 and 10
    multiplier = random.randint(1, 10)

    # Calculate the array size as the base size multiplied by the multiplier
    array_size = base_size * multiplier

    # Clamp the array size between 4 and 10000
    return max(4, min(array_size, 10000))

