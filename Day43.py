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

aa = bingo[0][0]
ab = bingo[0][1]
ac = bingo[0][2]
ba = bingo[1][0]
bb = bingo[1][1]
bc = bingo[1][2]
ca = bingo[2][0]
cb = bingo[2][1]
cc = bingo[2][2]


print(f"{aa:^5}|{ab:^5}|{ac:^5}")
print("--------------------")
print(f"{ba:^5}|{bb:^5}|{bc:^5}")
print("--------------------")
print(f"{ca:^5}|{cb:^5}|{cc:^5}")
