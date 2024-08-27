print("Multiplication Table")

multiples = int(input("Enter your multiples: "))
correct = 0

for i in range(1, 11):
    user_input = int(input(f"{i} * {multiples} = "))

    if user_input == i * multiples:
        print("Correct")
        correct += 1
    else:
        print(f"Incorrect. {i} * {multiples} = {i * multiples}")

print(f"You got {correct} correct.")
if correct == 10:
    print("You win!")
if correct <= 5:
    print("Better luck next time!")
