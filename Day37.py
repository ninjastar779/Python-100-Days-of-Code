print("STAR WARS NAME GENERATOR")

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
maiden = input("Enter your mother's maiden name: ").strip()
city = input("Enter the city you were born: ").strip()

name = f"{first[:3].title()}{last[:2].lower()} {maiden[:2].title()}{city[-3:]}"

print("Your star wars name is: " + name)