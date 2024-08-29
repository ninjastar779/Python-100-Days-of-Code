names = []

while True:
    firstName = input("Enter the first name: ").strip(" ").capitalize()
    lastName = input("Enter the last name: ").strip(" ").capitalize()
    name = f"{firstName} {lastName}"
    if name in names:
        print("This name is already in the list.")
    else:
        names.append(name)

    for name in names:
        print(name)