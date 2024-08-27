import random, os, time
print("Random Character Generator")

def rollDice(sides):
    return random.randint(1, sides)

def health():
    return (rollDice(6) + rollDice(12)) // 2 + 10

def strength():
    return (rollDice(6) + rollDice(8)) // 2 + 12

while True:
    p1name = input("What is your name? ")
    charType = input("Character type? ")

    print(p1name)
    p1health = health()
    p1strength = strength()

    print()

    p2name = input("Who is your opponent? ")
    p2health = health()
    p2strength = strength()

    print()

    while True:
        time.sleep(2)
        os.system("cls")
        print("BATTLE TIME!")
        print("The battle has begun!")

        time.sleep(2)
        os.system("cls")
        print("Your character stats:")
        print("Name: " + p1name)
        print("Health: " + str(p1health))
        print("Strength: " + str(p1strength))

        time.sleep(2)
        os.system("cls")
        print(p2name + "'s character stats:")
        print("Name: " + p2name)
        print("Health: " + str(p2health))
        print("Strength: " + str(p2strength))

        time.sleep(2)
        os.system("cls")

        c1Dice = rollDice(6)
        c2Dice = rollDice(6)

        if c1Dice > c2Dice:
            print(f"{p1name} hits a blow to {p2name}!")
            difference = abs(p1strength - p2health) + 1
            p2health -= difference
            print(f"{p2name} has {p2health} health remaining.")

        elif c1Dice < c2Dice:
            print(f"{p2name} hits a blow to {p1name}!")
            difference = abs(p2strength - p1health) + 1
            p1health -= difference
            print(f"{p1name} has {p1health} health remaining.")

        if p1health <= 0:
            print(f"{p1name} has been defeated!")
            print(f"{p2name} wins!")
            break

        elif p2health <= 0:
            print(f"{p2name} has been defeated!")
            print(f"{p1name} wins!")
            break

    break

