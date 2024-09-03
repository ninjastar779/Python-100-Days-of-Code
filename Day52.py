pizzas = []


def save_pizzas():
    with open("pizza.txt", "w") as f:
        for pizza in pizzas:
            f.write(",".join([str(x) for x in pizza]) + "\n")


def load_pizzas():
    global pizzas
    try:
        with open("pizza.txt", "r") as f:
            pizzas = []
            for line in f:
                pizzas.append([x.strip() for x in line.split(",")])
    except FileNotFoundError:
        pass


def pretty_print_pizzas(pizzas):
    for pizza in pizzas:
        print(
            f"Name: {pizza[0]}, Size: {pizza[2]}, Price: ${pizza[4]}, Toppings: {pizza[1]}"
        )


load_pizzas()

while True:
    print("1. Add pizza")
    print("2. View pizzas")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        toppings = input("Enter toppings: ")
        size = input("Enter size (small/medium/large): ")
        quantity = int(input("Enter quantity: "))
        total = 0
        if size == "small":
            total = 5 * quantity
        elif size == "medium":
            total = 10 * quantity
        elif size == "large":
            total = 12 * quantity
        else:
            print("Invalid size")
            continue
        pizzas.append([name, toppings, size, quantity, total])
        save_pizzas()
        print("Total: ${:.2f}".format(total))
    elif choice == "2":
        pretty_print_pizzas(pizzas)
    else:
        print("Invalid choice")
    option = input("Do you want to continue? (y/n): ")
    if option.lower() != "y":
        break
