def add_todo():
    """
    Asks the user to enter a new todo item and its properties, and adds it to the list of todos
    """
    todo = input("Enter your todo: ")
    due = input("Enter when your todo is due: ")
    priority = input("Enter the priority of your todo (low, medium, high): ")
    todos.append({"todo": todo, "due": due, "priority": priority})


def view_todos():
    """
    Asks the user whether they want to view all todos or a specific priority of todos,
    and then prints out all of the todos or the specific priority of todos that the user asked for
    """

    choice = input(
        "Do you want to view all or a specific priority of todos? (all, low, medium, high): "
    )
    if choice == "all":
        for i, todo in enumerate(todos, 1):
            print(
                f"{i}. {todo['todo']} - Due: {todo['due']} - Priority: {todo['priority']}"
            )
    else:
        for i, todo in enumerate(
            [todo for todo in todos if todo["priority"] == choice], 1
        ):
            print(
                f"{i}. {todo['todo']} - Due: {todo['due']} - Priority: {todo['priority']}"
            )


def edit_todo():
    """
    Asks the user for the number of the todo they want to edit, and new values for the todo, due date, and priority,
    and then edits the todo with those new values
    """
    choice = int(input("Enter the number of the todo you want to edit: ")) - 1
    todo = input("Enter the new todo: ")
    due = input("Enter the new due date: ")
    priority = input("Enter the new priority: ")
    todos[choice]["todo"] = todo
    todos[choice]["due"] = due
    todos[choice]["priority"] = priority


def remove_todo():
    """
    Asks the user for the number of the todo they want to remove, and then removes it from the list of todos
    """
    choice = int(input("Enter the number of the todo you want to remove: ")) - 1
    del todos[choice]


todos = []
while True:
    print("\n1. Add a todo")
    print("2. View todos")
    print("3. Edit a todo")
    print("4. Remove a todo")
    print("5. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_todo()
    elif choice == "2":
        view_todos()
    elif choice == "3":
        edit_todo()
    elif choice == "4":
        remove_todo()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
