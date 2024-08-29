todo_list = []
print("To-Do List")

def add_item(item):
    todo_list.append(item)

def view_list():
    for item in todo_list:
        print(item)

def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
    else:
        print("Item not found in list")

while True:
    print("\n1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter item to add: ")
        add_item(item)
    elif choice == "2":
        view_list()
    elif choice == "3":
        item = input("Enter item to remove: ")
        remove_item(item)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
