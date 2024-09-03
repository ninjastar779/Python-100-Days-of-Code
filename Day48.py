print("HIGH SCORE TABLE")

while True:
    initials = input("Please enter your initials: ").strip().upper()[0:3]
    score = int(input("Please enter your score: "))

    if score > 100000:
        print("Your score must be less than 100,000")
        continue

    f = open("scores.txt", "a+")

    f.write(initials + " " + str(score) + "\n")

    cont = input("Would you like to enter another score? (y/n) ")

    if cont.lower() != "y":
        break

f.close()