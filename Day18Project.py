import random

print("Guess a number between 1 and 1000000")

number = random.randint(1, 1000000)

guesses = 0

while True:
    guess = int(input("> "))
    guesses += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print(f"Correct! It took you {guesses} guesses")
        break