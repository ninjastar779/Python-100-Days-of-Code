import os
import random

try:
    with open("todo_list.txt", "r") as f:
        todo_list = [line.strip() for line in f]
except FileNotFoundError:
    todo_list = []

def add_item(item):
    if item not in todo_list:
        todo_list.append(item)
    else:
        print("Item already exists in list.")
    save_list()

def remove_item(item):
    if item in todo_list:
        confirm = input(f"Are you sure you want to remove {item}? (y/n): ")
        if confirm.lower() == "y":
            todo_list.remove(item)
        else:
            print("Item not removed.")
    else:
        print("Item not found in list.")
    save_list()

def clear_list():
    confirm = input("Are you sure you want to clear the entire list? (y/n): ")
    if confirm.lower() == "y":
        del todo_list[:]
    else:
        print("List not cleared.")
    save_list()

def view_list():
    if len(todo_list) == 0:
        print("The list is empty.")
    else:
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}")

def save_list():
    with open("todo_list.txt", "w") as f:
        for item in todo_list:
            f.write(item + "\n")

    # create a backup folder and a random file name
    backup_folder = "backups"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    random_file_name = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}.txt"
    backup_file = os.path.join(backup_folder, random_file_name)

    # save a copy of the file in the backup folder
    with open(backup_file, "w") as f:
        for item in todo_list:
            f.write(item + "\n")

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Clear list")
    print("4. View list")
    print("5. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter item to remove: ")
        remove_item(item)
    elif choice == "3":
        clear_list()
    elif choice == "4":
        view_list()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
