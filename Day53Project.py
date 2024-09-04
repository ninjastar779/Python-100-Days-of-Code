try:
    f = open("inventory.txt", "r")
    inventory = [line.strip() for line in f]
except FileNotFoundError:
    inventory = []

while True:
    print("INVENTORY\n")
    print("=========\n")

    option = input("1: Add item\n2: Remove item\n3: View inventory\n4: Quit\n")

    if option not in ["1", "2", "3", "4"]:
        print("Invalid option")
        continue

    if option == "1":
        item = input("Enter item: ")
        inventory.append(item.title())
        print("Item added")
        continue

    if option == "2":
        item = input("Enter item: ")
        if item in inventory:
            inventory.remove(item)
            print("Item removed")
        else:
            print("Item not found")
        continue

    if option == "3":
        counts = {}
        for item in inventory:
            counts[item] = counts.get(item, 0) + 1
        for item, count in counts.items():
            print(f"{item}: {count}")
        print()
        if not counts:
            print("Inventory is empty")
        continue


    if option == "4":
        break


f = open("inventory.txt", "w")
for item in inventory:
    f.write(item + "\n")
f.close()