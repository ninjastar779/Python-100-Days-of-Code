beasts = {}

while True:
    beast = {
        "Type": None,
        "Special Move": None,
        "HP": None,
        "MP": None,
    }
    type = ["Fire", "Water", "Earth", "Air", "Spirit"]

    name = input("Enter the name of the beast: ")
    for key, value in beast.items():
        beast[key] = input(f"Enter {key}: ")

    beasts[name] = beast

    print()

    for key, value in beast.items():
        if beast["Type"] == type[0]:
            print("\033[31m", end="")
        elif beast["Type"] == type[1]:
            print("\033[34m", end="")
        elif beast["Type"] == type[2]:
            print("\033[32m", end="")
        elif beast["Type"] == type[3]:
            print("\033[35m", end="")
        elif beast["Type"] == type[4]:
            print("\033[37m", end="")
        else:
            print("\033[0m", end="")

        print(f"{key}: {value}")
    print()

    print("\033[0m", end="")

    if input("Do you want to enter another beast? (Y/N): ").lower() == "n":
        break

def pretty_print_beasts(beasts):
    for name, beast in beasts.items():
        print(f"{name}: {beast}")

pretty_print_beasts(beasts)
