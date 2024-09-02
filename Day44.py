import random


bingo = []


def ran():
    """
    Returns a random integer between 1 and 99.

    Returns:
        int: A random integer between 1 and 99.
    """
    number = random.randint(1, 99)
    return number


for i in range(3):
    sublist = []
    for j in range(3):
        j = ran()
        sublist.append(j)
    bingo.append(sublist)


bingo[1][1] = "BINGO"


def print_bingo_card():
    """Prints the current state of the bingo card."""
    for row in bingo:
        print(f"{row[0]:^5}|{row[1]:^5}|{row[2]:^5}")
        print("--------------------")


def check_called_number(called_number):
    """Marks the number as an 'X' in the bingo card if it exists."""
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == called_number:
                bingo[i][j] = "X"


def check_for_win():
    """
    Checks if the game has been won by checking if all non-"BINGO" elements
    in the bingo card are equal to "X".

    The function works by iterating over each row in the bingo card, and
    then iterating over each element in the row. It checks if the element
    is not equal to "BINGO", and if so, checks if it is equal to "X". If
    all elements that are not "BINGO" are "X", the function returns True,
    indicating that the game has been won.

    Returns:
        bool: True if the game has been won, False otherwise.
    """
    return all(x == "X" for row in bingo for x in row if x != "BINGO")


while True:
    print_bingo_card()
    called_number = int(input("Enter the number that has been called: "))
    check_called_number(called_number)
    if check_for_win():
        print("BINGO!!!")
        break
