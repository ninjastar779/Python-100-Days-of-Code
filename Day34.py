print("SPAMMER INC.")

emails = []

while True:
    print("1. Add email")
    print("2. View emails")
    print("3. Remove email")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        email = input("Enter email: ")
        emails.append(email)

    elif choice == "2":
        for email in emails:
            print(email)

    elif choice == "3":
        email = input("Enter email: ")
        if email in emails:
            emails.remove(email)
        else:
            print("Email not found")

    elif choice == "4":
        break
    else:
        print("Invalid choice")

    print()

print("Goodbye!")
