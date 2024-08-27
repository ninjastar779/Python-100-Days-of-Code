print("Character Stat Generator")

def healthGenerator():
    """
    Generate a random health value for a character.

    This function generates a random health value for a character by multiplying
    two random integers between 1 and 6 and 1 and 8. The resulting health value is
    then returned.

    Returns:
        An integer representing the randomly generated health value for the character.
    """
    import random
    health = random.randint(1, 6) * random.randint(1, 8)
    return health

name = input("What is your name?: ")
print(name + " has " + str(healthGenerator()) + " health.")