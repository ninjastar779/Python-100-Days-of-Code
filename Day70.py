import secrets

users = {
    "admin": {"password": secrets.token_hex(16), "role": "admin"},
    "user": {"password": secrets.token_hex(16), "role": "user"}
}
def login(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    else:
        return None

print("Login Page")
# print(users["user"]["password"]) For testing
# print(users["admin"]["password"]) For testing
username = input("Username: ")
password = input("Password: ")
role = login(username, password)
print(f"Hello, {role}!" if role else "Invalid credentials")
