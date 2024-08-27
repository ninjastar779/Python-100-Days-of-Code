# The range function generates a sequence of numbers from start (inclusive)
# to stop (exclusive), by default with a step of 1.
# The for loop then iterates over each number in the generated sequence.

# The f-string is used to format the output string.
# <3 is a format specifier that left-aligns the value of i with a width of 3.

# The range function generates numbers from 1 to 30 (exclusive).
# The print function then displays the formatted output string for each number.

for i in range(1, 31):
    print(f"Day {i: <3} of 100.")