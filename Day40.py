name = input("Enter your name: ")
birthdate = input("Enter your birthday: ")
telNum = input("Enter your phone number: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

user_info = {"Name": name, "DOB": birthdate, "Phone Number": telNum, "Email": email, "Address": address}

for key, value in user_info.items():
    print(key + ":", value)
