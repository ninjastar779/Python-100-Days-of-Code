print("Monke Beast")
beast = {
    "Name of the beast": None,
    "Type": None,
    "Special Move": None,
    "HP": None,
    "MP": None,
}
type = ["Fire", "Water", "Earth", "Air", "Spirit"]

for name, value in beast.items():
    beast[name] = input(f"Enter {name}: ")
print()

for name, value in beast.items():
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

for name, value in beast.items():
    print(f"{name}: {value}")
print()

print("\033[0m", end="")
