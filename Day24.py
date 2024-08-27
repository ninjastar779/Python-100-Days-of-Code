print("Infinity Dice")

def dice(sides):
    """
    Roll a dice with a given number of sides.

    Parameters:
        sides (int): The number of sides the dice has.

    Returns:
        int: A random integer between 1 and the number of sides.
    """
    import random
    return random.randint(1, sides)

sides = int(input("Enter the number of sides: "))
while True:
    print(dice(sides))
    option = input("Roll again? (y/n): ")
    if option.lower() != "y":
        exit()