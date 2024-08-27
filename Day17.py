while True:
    print("You are at a fork in the road. Which way would you like to go? (left/right)")
    direction = input("> ")

    if direction == "left":
        print("You have fallen!")
        break
    elif direction == "right":
        continue
    else:
        print("You're a genius! You win!")
        exit()
print("The game is over, you failed.")