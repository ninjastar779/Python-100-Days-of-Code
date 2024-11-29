from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Template</title>
</head>

<body>
    <form action="/login" method="post">
        <p>Username: <input type="text" name="username"></p>
        <p>Email Address: <input type="email" name="email"></p>
        <p>Password: <input type="password" name="password"></p>
        <p><input type="submit" value="Submit"></p>
    </form>
</body>

</html>"""

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    logins = {
        "admin": {"email": "FyQHt@example.com", "password": "admin123"},
        "user": {"email": "zqLQK@example.com", "password": "user123"}
    }

    if username in logins and logins[username]["email"] == email and logins[username]["password"] == password:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run(debug=True)