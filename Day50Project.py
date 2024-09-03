import random, os, time

f = open("big.ideas", "a+")

while True:
    print("BIG IDEAS\n")
    option = input("1: Add Idea\n2: View Random Idea\n3: Quit\n")

    if option not in ["1", "2", "3"]:
        print("Invalid Option")
        time.sleep(1)
        os.system("cls")
        continue

    os.system("cls")

    if option == "1":
        idea = input("Enter Idea: ")
        f.write(idea + "\n")
        print("Idea Added!")
        time.sleep(1)
        os.system("cls")

    if option == "2":
        f.seek(0)
        lines = f.readlines()
        idea = random.choice(lines)
        print(f"Random Idea: {idea.strip()}")
        time.sleep(3)
        os.system("cls")

    if option == "3":
        f.close()
        break
