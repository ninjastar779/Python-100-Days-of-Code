from getpass import getpass as input

print("Welcome to Rock, Paper, Scissors!")

player1choice = input("Player 1, enter your choice (R, P, or S): ")

player2choice = input("Player 2, enter your choice (R, P, or S): ")

if player1choice == "R":
    print("Rock...")
elif player1choice == "P":
    print("Paper...")
elif player1choice == "S":
    print("Scissors...")
else:
    print("Invalid choice. Please enter R, P, or S.")

print("...vs...")

if player2choice == "R":
    print("Rock!")
elif player2choice == "P":
    print("Paper!")
elif player2choice == "S":
    print("Scissors!")
else:
    print("Invalid choice. Please enter R, P, or S.")

if player1choice == player2choice:
    print("It's a tie!")
elif player1choice == "R":
    if player2choice == "P":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
elif player1choice == "P":
    if player2choice == "S":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
elif player1choice == "S":
    if player2choice == "R":
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")
else:
    print("Invalid choice. Please enter R, P, or S.")